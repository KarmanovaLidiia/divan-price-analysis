import numpy as np
import matplotlib.pyplot as plt

# Шаг 1: параметры распределения
mean = 0        # среднее значение
std_dev = 1     # стандартное отклонение
num_samples = 1000  # сколько чисел сгенерировать

# Шаг 2: генерация случайных данных
data = np.random.normal(mean, std_dev, num_samples)

# Шаг 3: создаём гистограмму
plt.hist(data, bins=30, edgecolor='black')  # 30 «столбиков»

# Шаг 4: оформляем график
plt.title("Гистограмма нормального распределения")
plt.xlabel("Значение")
plt.ylabel("Частота")

# Шаг 5: сохраняем график в файл
plt.savefig("normal_histogram.png")
print("✅ Гистограмма сохранена как 'normal_histogram.png'")
