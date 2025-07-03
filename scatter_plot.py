import numpy as np
import matplotlib.pyplot as plt

# Шаг 1: создаём два набора случайных чисел
x = np.random.rand(50)
y = np.random.rand(50)

# Шаг 2: строим scatter plot
plt.scatter(x, y)

# Шаг 3: оформляем
plt.title("Диаграмма рассеяния")
plt.xlabel("X")
plt.ylabel("Y")

# Шаг 4: сохраняем
plt.savefig("scatter_plot.png")
print("✅ Диаграмма рассеяния сохранена как 'scatter_plot.png'")
