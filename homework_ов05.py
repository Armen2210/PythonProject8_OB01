# -*- coding: utf-8 -*-
# Игра: "Охотник и монстры" — с синтезированными звуками
# Запуск: python main.py

import math
import random
import sys
from array import array
import pygame

# -------------------- Экран и цвета --------------------
WIDTH, HEIGHT = 900, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 60

WHITE  = (255, 255, 255)
BGREEN = (16, 120, 16)
GREEN  = (70, 200, 90)
BLACK  = (0, 0, 0)
YELLOW = (235, 200, 40)
RED    = (210, 60, 60)
GRAY   = (110, 110, 110)

# -------------------- Параметры игры --------------------
BASE_BUSHES = 4
BASE_MONSTERS = 1
BUSH_SIZE = (54, 28)
BORDER_PADDING = 8

HUNTER_RADIUS = 18
HUNTER_BARREL_LEN = 28
HUNTER_TURN_LERP = 0.2
RECOIL_PIXELS = 8
RECOIL_DECAY = 0.8

MONSTER_RADIUS = 14
MONSTER_BASE_SPEED = 1.45
MONSTER_SPEED_UP_PER_LEVEL = 0.09
MONSTER_WOBBLE = 0.18

BLAST_RANGE = 200
SPREAD_DEG = 60
KILLS_PER_SHOT = 2

EMERGE_MIN_FRAMES = 20
EMERGE_MAX_FRAMES = 70

CONE_ALPHA = 28
MUZZLE_FLASH_TIME = 6
SHAKE_ON_SHOT = 4
SHAKE_ON_HIT  = 8

PARTICLES_PER_KILL = 10
LEAF_COLOR = (38, 160, 60)

MINI_RADAR_MARGIN = 10
FONT_NAME = None

random.seed()

# -------------------- Аудио: синтез и менеджер --------------------
def _make_buffer(samples):
    """Преобразует массив array('h') в bytes для Sound(buffer=...)."""
    return samples.tobytes()

def synth_tone(freq_hz=440, ms=120, vol=0.6, sample_rate=44100):
    """Синус/эксп-спад (удар), 16-bit mono."""
    total = int(sample_rate * ms / 1000)
    data = array('h')
    two_pi_f = 2 * math.pi * freq_hz / sample_rate
    for n in range(total):
        # экспоненциальный спад для «ударности»
        env = math.exp(-3.5 * n / total)
        s = math.sin(two_pi_f * n) * env
        val = int(max(-1.0, min(1.0, s * vol)) * 32767)
        data.append(val)
    return _make_buffer(data)

def synth_noise(ms=90, vol=0.5, sample_rate=44100, lowpass=0.35):
    """Белый шум с лёгким низкочастотным фильтром — для дробовика/шороха."""
    total = int(sample_rate * ms / 1000)
    data = array('h')
    x = 0.0
    for n in range(total):
        # простейший 1-полюсный НЧ-фильтр
        x = (1 - lowpass) * x + lowpass * (random.uniform(-1, 1))
        env = math.exp(-3.0 * n / total)
        val = int(max(-1.0, min(1.0, x * env * vol)) * 32767)
        data.append(val)
    return _make_buffer(data)

def mix_buffers(*bufs):
    """Смешивает несколько 16-бит моно буферов одинаковой длины (по минимальному)."""
    if not bufs: return b""
    parts = [array('h', b) for b in bufs]
    length = min(len(p) for p in parts)
    out = array('h', [0]*length)
    for i in range(length):
        s = 0
        for p in parts:
            s += p[i]
        # мягкий клиппинг
        s = max(-32767, min(32767, s))
        out[i] = s
    return _make_buffer(out)

class SoundManager:
    def __init__(self):
        self.enabled = False
        # Настраиваем микшер под 44.1kHz, 16-бит, моно
        try:
            pygame.mixer.pre_init(44100, -16, 1, 256)
            pygame.mixer.init()
            self.enabled = True
        except Exception:
            self.enabled = False
            return

        # Заготавливаем звуки
        try:
            # дробовик: шум + ударная «щёлка»
            shot_noise = synth_noise(ms=95, vol=0.7, lowpass=0.45)
            shot_click = synth_tone(freq_hz=2200, ms=20, vol=0.5)
            self.s_shot = pygame.mixer.Sound(buffer=mix_buffers(shot_noise, shot_click))
            self.s_shot.set_volume(0.9)

            # попадание: глухой «поп»
            self.s_hit  = pygame.mixer.Sound(buffer=synth_tone(freq_hz=220, ms=80, vol=0.7))
            self.s_hit.set_volume(0.6)

            # шорох куста при выходе
            self.s_rustle = pygame.mixer.Sound(buffer=synth_noise(ms=140, vol=0.5, lowpass=0.55))
            self.s_rustle.set_volume(0.5)

            # шаг монстра: низкий «тумп»
            self.s_step = pygame.mixer.Sound(buffer=synth_tone(freq_hz=110, ms=45, vol=0.6))
            self.s_step.set_volume(0.55)

            # победа/проигрыш — короткие сигналы
            self.s_win  = pygame.mixer.Sound(buffer=mix_buffers(
                synth_tone(660, 90, 0.6), synth_tone(990, 90, 0.4)))
            self.s_fail = pygame.mixer.Sound(buffer=synth_tone(140, 300, 0.5))
        except Exception:
            # на случай редких несовпадений форматов
            self.enabled = False

    def play(self, snd, volume=None):
        if not self.enabled or snd is None: return
        if volume is not None:
            v_old = snd.get_volume()
            snd.set_volume(max(0.0, min(1.0, volume)))
            snd.play()
            snd.set_volume(v_old)
        else:
            snd.play()

    # удобные методы
    def shot(self):   self.play(self.s_shot)
    def hit(self):    self.play(self.s_hit)
    def rustle(self): self.play(self.s_rustle)
    def win(self):    self.play(self.s_win)
    def fail(self):   self.play(self.s_fail)
    def step(self, vol=0.5): self.play(self.s_step, volume=vol)

# -------------------- Утилиты --------------------
def clamp(v, lo, hi): return max(lo, min(v, hi))
def vec(a, b): return (b[0] - a[0], b[1] - a[1])
def length(v): return math.hypot(v[0], v[1])
def normalize(v):
    l = length(v)
    return (0, 0) if l == 0 else (v[0] / l, v[1] / l)

def lerp_angle(a, b, t):
    diff = math.atan2(math.sin(b - a), math.cos(b - a))
    return a + diff * t

def angle_to(a, b): return math.atan2(b[1] - a[1], b[0] - a[0])
def deg_diff(a, b): return (a - b + 180) % 360 - 180

def rects_on_edges(count):
    if count <= 0: return []
    positions = []
    per_side = max(1, count // 4)
    extras = count % 4
    sides_counts = [per_side] * 4
    for i in range(extras): sides_counts[i] += 1
    w, h = BUSH_SIZE
    # TOP
    n = sides_counts[0]
    if n > 0:
        step = (WIDTH - 2 * BORDER_PADDING - w) / max(1, n - 1) if n > 1 else 0
        for i in range(n):
            x = BORDER_PADDING + i * step
            y = BORDER_PADDING
            positions.append((int(x), int(y), w, h))
    # RIGHT
    n = sides_counts[1]
    if n > 0:
        step = (HEIGHT - 2 * BORDER_PADDING - h) / max(1, n - 1) if n > 1 else 0
        for i in range(n):
            x = WIDTH - BORDER_PADDING - w
            y = BORDER_PADDING + i * step
            positions.append((int(x), int(y), w, h))
    # BOTTOM
    n = sides_counts[2]
    if n > 0:
        step = (WIDTH - 2 * BORDER_PADDING - w) / max(1, n - 1) if n > 1 else 0
        for i in range(n):
            x = BORDER_PADDING + i * step
            y = HEIGHT - BORDER_PADDING - h
            positions.append((int(x), int(y), w, h))
    # LEFT
    n = sides_counts[3]
    if n > 0:
        step = (HEIGHT - 2 * BORDER_PADDING - h) / max(1, n - 1) if n > 1 else 0
        for i in range(n):
            x = BORDER_PADDING
            y = BORDER_PADDING + i * step
            positions.append((int(x), int(y), w, h))
    return positions

# -------------------- Визуальные помощники --------------------
def draw_vignette(surface):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (0, 0, 0, 35), (0, 0, WIDTH, HEIGHT), border_radius=18)
    surface.blit(overlay, (0, 0))

def draw_shadow_circle(surf, pos, r):
    s = pygame.Surface((r*2+6, r*2+6), pygame.SRCALPHA)
    pygame.draw.circle(s, (0,0,0,45), (r+3, r+6), r)
    surf.blit(s, (pos[0]-r-3, pos[1]-r-3))

def draw_cone(surf, origin, ang, fov_deg, dist, alpha):
    half = math.radians(fov_deg/2)
    left = ang - half
    right = ang + half
    tip = origin
    left_pt = (origin[0] + math.cos(left)*dist, origin[1] + math.sin(left)*dist)
    right_pt = (origin[0] + math.cos(right)*dist, origin[1] + math.sin(right)*dist)
    poly = [tip, left_pt, right_pt]
    cone = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.polygon(cone, (255, 200, 0, alpha), poly)
    surf.blit(cone, (0,0))

def draw_arrow_hint(surf, from_center_to, color=(200,0,0)):
    dx, dy = from_center_to
    if dx == 0 and dy == 0: return
    ang = math.atan2(dy, dx)
    t = 1e9
    if math.cos(ang) != 0:
        t = min(t, (WIDTH - MINI_RADAR_MARGIN - CENTER[0]) / math.cos(ang) if dx>0
                  else (MINI_RADAR_MARGIN - CENTER[0]) / math.cos(ang))
    if math.sin(ang) != 0:
        t = min(t, (HEIGHT - MINI_RADAR_MARGIN - CENTER[1]) / math.sin(ang) if dy>0
                  else (MINI_RADAR_MARGIN - CENTER[1]) / math.sin(ang))
    px = CENTER[0] + math.cos(ang)*t
    py = CENTER[1] + math.sin(ang)*t
    p = (int(px), int(py))
    s = pygame.Surface((24,24), pygame.SRCALPHA)
    tip = (12 + math.cos(ang)*10, 12 + math.sin(ang)*10)
    left = (12 + math.cos(ang+2.5)*8, 12 + math.sin(ang+2.5)*8)
    right= (12 + math.cos(ang-2.5)*8, 12 + math.sin(ang-2.5)*8)
    pygame.draw.polygon(s, color, [tip,left,right])
    surf.blit(s, (p[0]-12, p[1]-12))

# -------------------- Частицы --------------------
class Particle:
    def __init__(self, pos, vel, life, color):
        self.x, self.y = pos
        self.vx, self.vy = vel
        self.life = life
        self.color = color
        self.r = random.randint(2,4)
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.98
        self.vy = self.vy*0.98 + 0.15
        self.life -= 1
    def draw(self, surf):
        if self.life > 0:
            pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.r)

class FloatingText:
    def __init__(self, text, pos, color, life=40):
        self.text = text
        self.x, self.y = pos
        self.color = color
        self.life = life
        self.vy = -0.6
    def update(self):
        self.y += self.vy
        self.life -= 1
    def draw(self, surf, font):
        if self.life <= 0: return
        img = font.render(self.text, True, self.color)
        surf.blit(img, (self.x - img.get_width()//2, self.y - img.get_height()//2))

# -------------------- Экранный шейк --------------------
class ScreenShake:
    def __init__(self): self.power = 0.0
    def add(self, amount): self.power = min(20, self.power + amount)
    def offset(self):
        if self.power <= 0: return (0,0)
        ox = random.uniform(-self.power, self.power)
        oy = random.uniform(-self.power, self.power)
        self.power *= 0.85
        if self.power < 0.2: self.power = 0
        return (int(ox), int(oy))

# -------------------- Сущности --------------------
class Bush:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.swing_phase = random.random()*math.tau
    def draw(self, surf, rustle=0.0):
        sh = pygame.Surface((self.rect.w+10, self.rect.h+10), pygame.SRCALPHA)
        pygame.draw.ellipse(sh, (0,0,0,45), (0,0,self.rect.w+10, self.rect.h+10))
        surf.blit(sh, (self.rect.x-5, self.rect.y-2))

        sway = math.sin(self.swing_phase)*1.5
        body = self.rect.copy()
        body.inflate_ip(6, 8); body.move_ip(int(sway), 0)
        pygame.draw.ellipse(surf, BGREEN, body)
        pygame.draw.ellipse(surf, GREEN, body, 2)

        cx, _ = body.center
        r = max(8, body.height // 3)
        for dx in (-r, 0, r):
            pygame.draw.circle(surf, BGREEN, (cx+dx, body.top + r//2), r)
            pygame.draw.circle(surf, GREEN,  (cx+dx, body.top + r//2), r, 2)

        if rustle > 0:
            glow = pygame.Surface((body.w, body.h), pygame.SRCALPHA)
            pygame.draw.ellipse(glow, (255, 230, 120, int(80*rustle)), (0,0,body.w, body.h))
            surf.blit(glow, (body.x, body.y), special_flags=pygame.BLEND_PREMULTIPLIED)

        self.swing_phase += 0.02

class Monster:
    def __init__(self, pos, speed, emerge_timer_frames, bush_ref=None, sounds=None):
        self.x, self.y = pos
        self.speed = speed
        self.alive = True
        self.emerge_timer = emerge_timer_frames
        self.phase = random.random()*math.tau
        self.bush_ref = bush_ref
        self.sounds = sounds

        # аудио-стейт
        self._emerged_once = False
        self._step_timer = 0   # кадры до следующего шага

    @property
    def emerged(self):
        return self.emerge_timer <= 0

    def update(self, target_pos):
        if not self.alive: return
        if self.emerge_timer > 0:
            self.emerge_timer -= 1
            # если только что вышел — шорох
            if self.emerge_timer == 0 and not self._emerged_once:
                self._emerged_once = True
                if self.sounds: self.sounds.rustle()
            return

        # движение с «воблом»
        d = vec((self.x, self.y), target_pos)
        dirn = normalize(d)
        self.phase += 0.12
        wob = (math.cos(self.phase)*MONSTER_WOBBLE, math.sin(self.phase*0.5)*MONSTER_WOBBLE)
        vx = (dirn[0] + wob[0]) * self.speed
        vy = (dirn[1] + wob[1]) * self.speed
        self.x += vx; self.y += vy

        # шаги: период зависит от скорости
        self._step_timer -= 1
        if self._step_timer <= 0:
            self._step_timer = max(10, 34 - int(self.speed*8))
            if self.sounds:
                # громкость зависит от расстояния до охотника
                dist = length(vec((self.x, self.y), target_pos))
                vol = clamp(1.0 - dist/420.0, 0.08, 0.7)
                self.sounds.step(vol=vol)

    def draw(self, surf):
        if not self.alive: return
        color = RED if self.emerged else (220, 140, 140)
        draw_shadow_circle(surf, (int(self.x), int(self.y)), MONSTER_RADIUS)
        pygame.draw.circle(surf, color, (int(self.x), int(self.y)), MONSTER_RADIUS)
        pygame.draw.circle(surf, BLACK, (int(self.x)+3, int(self.y)-3), 3)

    def distance_to(self, pos): return length(vec((self.x, self.y), pos))
    def hits_hunter(self, hunter_pos):
        return self.alive and self.emerged and self.distance_to(hunter_pos) <= (MONSTER_RADIUS + HUNTER_RADIUS)

class Hunter:
    def __init__(self, pos):
        self.x, self.y = pos
        self.ang = 0.0
        self.recoil = 0.0
        self.muzzle_timer = 0

    def update_aim(self, mouse_pos):
        target_ang = angle_to((self.x, self.y), mouse_pos)
        self.ang = lerp_angle(self.ang, target_ang, HUNTER_TURN_LERP)
        self.recoil *= RECOIL_DECAY
        if self.muzzle_timer > 0: self.muzzle_timer -= 1

    def draw(self, surf, show_cone=False):
        if show_cone:
            draw_cone(surf, (self.x, self.y), self.ang, SPREAD_DEG, BLAST_RANGE, CONE_ALPHA)
        draw_shadow_circle(surf, (int(self.x), int(self.y)), HUNTER_RADIUS+2)
        pygame.draw.circle(surf, YELLOW, (int(self.x), int(self.y)), HUNTER_RADIUS)
        bl = HUNTER_BARREL_LEN - self.recoil
        end = (self.x + math.cos(self.ang) * bl, self.y + math.sin(self.ang) * bl)
        pygame.draw.line(surf, YELLOW, (self.x, self.y), end, 6)
        if self.muzzle_timer > 0:
            mf_end = (self.x + math.cos(self.ang) * (bl+10), self.y + math.sin(self.ang) * (bl+10))
            pygame.draw.circle(surf, (255,230,120), (int(mf_end[0]), int(mf_end[1])), 7)

# -------------------- Логика уровня --------------------
class Level:
    def __init__(self, number, sounds):
        self.number = number
        self.sounds = sounds
        self.bushes = [Bush(r) for r in rects_on_edges(BASE_BUSHES + (number - 1))]
        monsters_count = BASE_MONSTERS + (number - 1)
        speed = MONSTER_BASE_SPEED + (number - 1) * MONSTER_SPEED_UP_PER_LEVEL

        self.monsters = []
        for _ in range(monsters_count):
            b = random.choice(self.bushes).rect
            spawn_x = random.randint(b.left + 6, b.right - 6)
            spawn_y = random.randint(b.top + 6, b.bottom - 6)
            emerge_frames = random.randint(EMERGE_MIN_FRAMES, EMERGE_MAX_FRAMES)
            self.monsters.append(Monster((spawn_x, spawn_y), speed, emerge_frames, bush_ref=b, sounds=sounds))

        self.shots_left = monsters_count

    def alive_monsters(self): return [m for m in self.monsters if m.alive]
    def all_dead(self): return len(self.alive_monsters()) == 0
    def update(self, hunter_pos):
        for m in self.alive_monsters(): m.update(hunter_pos)

    def draw(self, surf):
        for b in self.bushes:
            rustle = 0.0
            for m in self.alive_monsters():
                if not m.emerged and m.bush_ref is not None and m.bush_ref == b.rect:
                    rustle = max(rustle, 1.0 - m.emerge_timer / max(1, EMERGE_MAX_FRAMES))
            b.draw(surf, rustle=rustle)
        for m in self.monsters: m.draw(surf)

    def shoot(self, hunter_pos, aim_ang, mouse_pos):
        if self.shots_left <= 0: return 0, []
        self.shots_left -= 1

        max_dist = BLAST_RANGE
        half_spread = SPREAD_DEG / 2.0
        look_deg = math.degrees(aim_ang)

        candidates = []
        for m in self.alive_monsters():
            if not m.emerged: continue
            v = vec(hunter_pos, (m.x, m.y)); dist = length(v)
            if dist == 0 or dist > max_dist: continue
            ang_deg = math.degrees(math.atan2(v[1], v[0]))
            if abs(deg_diff(ang_deg, look_deg)) <= half_spread:
                candidates.append((dist, m))

        if not candidates:
            for m in self.alive_monsters():
                if not m.emerged: continue
                if m.distance_to(mouse_pos) <= MONSTER_RADIUS + 6:
                    candidates.append((m.distance_to(hunter_pos), m))

        candidates.sort(key=lambda t: t[0])
        killed = []
        for _, m in candidates[:KILLS_PER_SHOT]:
            if m.alive:
                m.alive = False
                killed.append(m)
        return len(killed), killed

# -------------------- Основной цикл --------------------
def main():
    # важно: сначала mixer.pre_init/init в SoundManager, потом pygame.init()
    sounds = SoundManager()

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Охотник и монстры — со звуком")
    clock = pygame.time.Clock()
    font = pygame.font.Font(FONT_NAME, 20)
    big_font = pygame.font.Font(FONT_NAME, 36)
    small_font = pygame.font.Font(FONT_NAME, 16)

    hunter = Hunter(CENTER)
    level_num = 1
    level = Level(level_num, sounds)

    game_over = False
    level_cleared = False

    score = 0
    total_shots = 0
    total_kills = 0

    particles = []
    float_texts = []
    shake = ScreenShake()

    show_cone_soft = True
    cone_boost_timer = 0

    while True:
        mouse_pos = pygame.mouse.get_pos()

        # --- События ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if event.key == pygame.K_r:
                    if game_over:
                        game_over = False; level_cleared = False
                        level_num = 1; level = Level(level_num, sounds)
                        score = 0; total_shots = 0; total_kills = 0
                        particles.clear(); float_texts.clear()
                    elif level_cleared:
                        level_cleared = False
                        level_num += 1; level = Level(level_num, sounds)
                        particles.clear(); float_texts.clear()
                        if sounds.enabled: sounds.win()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not game_over and not level_cleared and level.shots_left > 0:
                    total_shots += 1
                    kills, killed_list = level.shoot((hunter.x, hunter.y), hunter.ang, mouse_pos)

                    # звук выстрела
                    if sounds.enabled: sounds.shot()

                    # визуальный фидбек
                    hunter.recoil = RECOIL_PIXELS
                    hunter.muzzle_timer = MUZZLE_FLASH_TIME
                    shake.add(SHAKE_ON_SHOT)

                    if kills > 0:
                        if sounds.enabled: sounds.hit()
                        total_kills += kills
                        base = 100; bonus = (kills-1)*75
                        add_score = base*kills + bonus
                        score += add_score
                        float_texts.append(FloatingText(f"+{add_score}", (mouse_pos[0], mouse_pos[1]-10), (20,140,20)))
                        for m in killed_list:
                            for _ in range(PARTICLES_PER_KILL):
                                ang = random.random()*math.tau
                                spd = random.uniform(1.2, 3.2)
                                particles.append(Particle((m.x, m.y),
                                                          (math.cos(ang)*spd, math.sin(ang)*spd-1.0),
                                                          random.randint(22,38),
                                                          LEAF_COLOR))
                    else:
                        float_texts.append(FloatingText("Промах", mouse_pos, (160,60,60)))

                    cone_boost_timer = 8

        # --- Логика ---
        if not game_over and not level_cleared:
            hunter.update_aim(mouse_pos)
            level.update((hunter.x, hunter.y))

            for m in level.alive_monsters():
                if m.hits_hunter((hunter.x, hunter.y)):
                    game_over = True
                    shake.add(SHAKE_ON_HIT)
                    float_texts.append(FloatingText("Охотник повержен", (WIDTH//2, HEIGHT//2-40), (160,40,40), life=80))
                    if sounds.enabled: sounds.fail()
                    break
            if level.all_dead():
                level_cleared = True
                float_texts.append(FloatingText("Уровень пройден!", (WIDTH//2, 90), (40,130,40), life=80))
                if sounds.enabled: sounds.win()

        # апдейты эффектов
        for p in particles[:]:
            p.update()
            if p.life <= 0: particles.remove(p)
        for ft in float_texts[:]:
            ft.update()
            if ft.life <= 0: float_texts.remove(ft)
        if cone_boost_timer > 0: cone_boost_timer -= 1

        # --- Рендер ---
        screen.fill(WHITE)
        pygame.draw.rect(screen, GRAY, (4, 4, WIDTH - 8, HEIGHT - 8), width=2, border_radius=8)

        ox, oy = ScreenShake.offset(shake)
        world = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        level.draw(world)

        alive = level.alive_monsters()
        if alive:
            nearest = sorted(alive, key=lambda m: m.distance_to(CENTER))[:3]
            for m in nearest:
                draw_arrow_hint(world, vec(CENTER, (m.x, m.y)))

        show_cone_now = True or cone_boost_timer > 0
        # конус рисуется внутри Hunter.draw при show_cone_now
        hunter.draw(world, show_cone=show_cone_now)

        for p in particles: p.draw(world)
        for ft in float_texts: ft.draw(world, font)
        draw_vignette(world)
        screen.blit(world, (ox, oy))

        # ---- UI ----
        ui_pad = 12
        shots_text = font.render(f"Патроны: {level.shots_left}", True, BLACK)
        mon_text   = font.render(f"Монстры: {len(level.alive_monsters())}", True, BLACK)
        lvl_text   = font.render(f"Уровень: {level.number}", True, BLACK)
        score_text = font.render(f"Счёт: {score}", True, BLACK)
        screen.blit(shots_text, (ui_pad, 12))
        screen.blit(mon_text,   (ui_pad, 36))
        screen.blit(lvl_text,   (ui_pad, 60))
        screen.blit(score_text, (ui_pad, 84))

        acc = (total_kills/total_shots*100) if total_shots>0 else 0.0
        acc_text = small_font.render(f"Точность: {acc:.0f}%  | Kills/Shot: {total_kills}/{total_shots}", True, (60,60,60))
        screen.blit(acc_text, (ui_pad, 112))

        hint = small_font.render("ЛКМ — выстрел | R — перезапуск/дальше | ESC — выход", True, BLACK)
        screen.blit(hint, (WIDTH - hint.get_width() - 12, 12))

        if game_over:
            over1 = big_font.render("ИГРА ОКОНЧЕНА", True, RED)
            over2 = font.render("Нажми R, чтобы начать сначала", True, BLACK)
            screen.blit(over1, ((WIDTH - over1.get_width()) // 2, HEIGHT // 2 - 40))
            screen.blit(over2, ((WIDTH - over2.get_width()) // 2, HEIGHT // 2 + 4))
        elif level_cleared:
            win1 = big_font.render("УРОВЕНЬ ПРОЙДЕН!", True, GREEN)
            win2 = font.render("Нажми R, чтобы перейти к следующему уровню", True, BLACK)
            screen.blit(win1, ((WIDTH - win1.get_width()) // 2, HEIGHT // 2 - 40))
            screen.blit(win2, ((WIDTH - win2.get_width()) // 2, HEIGHT // 2 + 4))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
