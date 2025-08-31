# import pygame
# pygame.init()
# import time
#
#
# window_size = (800, 600)  # размер окна
# screen = pygame.display.set_mode(window_size)  # создание окна
# pygame.display.set_caption("My game")  # название окна
#
# image1 = pygame.image.load("python_logo_80x80.png")  # загрузка изображения
# image_rect1 = image1.get_rect()  # Получаем прямоугольник. Чтобы изображение появилось на экране нужен цикл, иначе она появится только на одном кадре из многих.
#
# image2 = pygame.image.load("pycharm_logo_80x80.png")
# image_rect2 = image2.get_rect()
#
#
#
# # speed = 5 ## скорость перемещения изображения. Нужно для перемещения с помощью кнопок
#
# # "pygame.display" -для работы с окном, "pygame.image" - для работы с изображениями. Это отдельные модули: "pygame."
# # 2d объекты в pygame называются sprites
# # В данном случае упрощенный пример, при создании игр используются классы
#
# # цикл игры
# run = True
#
# while run:
#     for event in pygame.event.get():  # Обработка событий. Каждое отдельное событие сохраняется в переменную "event", а "pygame.event.get()" - список всех событий, последовательность.
#         if event.type == pygame.QUIT:  # Нажатие на крестик. Делаем переменную "run" равной "False", чтобы цикл завершался.
#             run = False
#         if event.type == pygame.MOUSEMOTION: # Перемещение мыши
#             mouseX, mouseY = pygame.mouse.get_pos()
#             image_rect1.x = mouseX - 40
#             image_rect1.y = mouseY - 40
#
#     if image_rect1.colliderect(image_rect2):  # Проверка столкновения. "colliderect" означает, что изображения сталкиваются
#         print("Коллизия, произошло столкновение!")
#         time.sleep(1) # Используется для паузы, чтобы не прописывалась многократно коллизия
#
#     # keys = pygame.key.get_pressed()  # Получаем список нажатых клавиш
#     # if keys[pygame.K_LEFT]:  # Если нажата клавиша влево
#     #     image_rect.x -= speed  # Перемещаем изображение влево
#     # if keys[pygame.K_RIGHT]:  # Если нажата клавиша вправо
#     #     image_rect.x += speed  # Перемещаем изображение вправо
#     # if keys[pygame.K_UP]:  # Если нажата клавиша вверх
#     #     image_rect.y -= speed  # Перемещаем изображение вверх
#     # if keys[pygame.K_DOWN]:  # Если нажата клавиша вниз
#     #     image_rect.y += speed  # Перемещаем изображение вниз
#     # Перемещение с помощью кнопок влево, вправо, вверх, вниз
#
#     screen.fill((0, 0, 0))  # Заполнение окна цветом(в данном случае черный). Формат: (R, G, B) - сначала красный, потом зеленый, потом синий.
#     screen.blit(image1, image_rect1) # Добавление изображения на экран. Делается строго после заполнения окна.
#     screen.blit(image2, image_rect2) # Добавление второго изображения на экран. Делается строго после заполнения окна.
#
#     pygame.display.flip()  # Обновление экрана. Делается после заполнения окна. Это необходимо, чтобы изменения на экране отобразились. Можно использовать "update" вместо "flip".
#
# pygame.quit()

# Эта вся основа которая могла быть нужна для разработки чего-либо

# Написание игры "арканоид"

import pygame
import sys

pygame.init()

# Окно
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Арканоид")

# Кирпичи
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 20
brick_gap = 5
bricks = [
    (col * (brick_width + brick_gap), row * (brick_height + brick_gap))
    for row in range(brick_rows) for col in range(brick_cols)
]

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
fps = 60

# Платформа
paddle_width, paddle_height = 100, 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 20
paddle_speed = 6

# Мяч
ball_radius = 8
ball_x = paddle_x + paddle_width // 2
ball_y = paddle_y - ball_radius
ball_speed_x = 4
ball_speed_y = -4

# ДОБАВЛЕНО: флаг «мяч запущен»
ball_released = False  # пока False — мяч «лежит» на платформе и двигается вместе с ней

def clamp(val, lo, hi):
    return max(lo, min(val, hi))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ДОБАВЛЕНО: управление мышью
        if event.type == pygame.MOUSEMOTION:
            # двигаем платформу по X под курсором
            mouse_x = event.pos[0]
            paddle_x = clamp(mouse_x - paddle_width // 2, 0, screen_width - paddle_width)
            # если мяч ещё не запущен — «держим» его на платформе
            if not ball_released:
                ball_x = paddle_x + paddle_width // 2
                ball_y = paddle_y - ball_radius

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # ЛКМ — запустить мяч
                ball_released = True
            if event.button == 3:  # ПКМ — вернуть мяч на платформу
                ball_released = False
                ball_x = paddle_x + paddle_width // 2
                ball_y = paddle_y - ball_radius
                ball_speed_x = 4
                ball_speed_y = -4

    # Клавиатура (оставлено как было)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # Если мяч не запущен — «прилипает» к платформе
    if not ball_released:
        ball_x = paddle_x + paddle_width // 2
        ball_y = paddle_y - ball_radius
    else:
        # Движение мяча
        ball_x += ball_speed_x
        ball_y += ball_speed_y

    # Столкновение со стенами (учёт радиуса)
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_speed_x = -ball_speed_x
        ball_x = clamp(ball_x, ball_radius, screen_width - ball_radius)

    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y
        ball_y = ball_radius

    if ball_y - ball_radius >= screen_height:
        # Потеря мяча — вернуть на платформу
        ball_released = False
        ball_x = paddle_x + paddle_width // 2
        ball_y = paddle_y - ball_radius
        ball_speed_x = 4
        ball_speed_y = -4

    # Столкновение с кирпичами
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    brick_rects = [pygame.Rect(bx, by, brick_width, brick_height) for (bx, by) in bricks]
    for i, brick_rect in enumerate(brick_rects):
        if brick_rect.colliderect(ball_rect) and ball_released:
            bricks.pop(i)
            ball_speed_y = -ball_speed_y
            break

    # Столкновение с платформой
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle_rect.colliderect(ball_rect) and ball_released:
        ball_speed_y = -abs(ball_speed_y)
        ball_y = paddle_y - ball_radius

    # Рендер
    screen.fill(BLACK)

    for bx, by in bricks:
        pygame.draw.rect(screen, WHITE, pygame.Rect(bx, by, brick_width, brick_height))

    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()







