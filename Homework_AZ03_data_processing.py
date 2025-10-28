import csv
import pandas as pd


def clean_price(price):
    price = price.replace('₽', '').replace('/мес.', '').replace(' ', '').replace(',', '').strip()

    if price == '' or price == '—':
        return None

    return int(price)


input_file = 'divan_prices.csv'
output_file = 'cleaned_divan_prices.csv'

cleaned_rows = []

with open(input_file, mode='r', encoding='utf-8') as infile, \
        open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)


    discount_index = header.index("Цена со скидкой")
    standard_index = header.index("Стандартная цена")


    writer.writerow(["Цена со скидкой", "Стандартная цена"])

    for row in reader:
        discounted = clean_price(row[discount_index])
        standard = clean_price(row[standard_index])

        if discounted is None and standard is None:
            continue

        if standard is None:
            standard = discounted

        cleaned_rows.append([discounted, standard])
        writer.writerow([discounted, standard])

print(f"✅ Обработанные данные сохранены в файл: {output_file}")

df = pd.DataFrame(cleaned_rows, columns=["Цена со скидкой", "Стандартная цена"])
avg_discounted = df["Цена со скидкой"].mean()
avg_standard = df["Стандартная цена"].mean()

print(f"Средняя цена со скидкой: {avg_discounted}₽")
print(f"Средняя цена стандартной стоимости: {avg_standard}₽")
