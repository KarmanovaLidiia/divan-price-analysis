import pandas as pd
import matplotlib.pyplot as plt

# Загружаем очищенные данные
data = pd.read_csv('divan_prices_cleaned.csv')

# Достаём столбец с ценами
prices = data['Price']

# Строим гистограмму
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=10, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (рубли)')
plt.ylabel('Частота')
plt.grid(True)

# Сохраняем график
plt.savefig('divan_price_histogram.png')
print("✅ Гистограмма сохранена в файл divan_price_histogram.png")
