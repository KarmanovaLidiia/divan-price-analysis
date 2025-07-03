import csv


def clean_price(text):
    # Удалим пробелы и "руб."
    text = text.replace("руб.", "").replace(" ", "").strip()
    # Иногда могут быть ошибки или пустые строки
    try:
        return int(text)
    except:
        return None  # Пропустить, если не число


input_file = 'divan_prices.csv'
output_file = 'divan_prices_cleaned.csv'

cleaned = []

with open(input_file, mode='r', encoding='utf-8') as infile, \
        open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)  # читаем заголовок
    writer.writerow(["Price"])  # сохраняем заголовок

    for row in reader:
        if row:
            number = clean_price(row[0])
            if number is not None:
                cleaned.append(number)
                writer.writerow([number])

# Вывод средней цены
if cleaned:
    avg_price = sum(cleaned) / len(cleaned)
    print(f"✅ Средняя цена дивана: {round(avg_price):,} руб.".replace(",", " "))
else:
    print("⚠️ Не удалось обработать данные.")
