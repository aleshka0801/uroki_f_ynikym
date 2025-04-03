import pandas as pd
import matplotlib.pyplot as plt

# Шаг 1: Считываем данные из Excel
file_path = 'data.xlsx'  # Путь к файлу Excel
df = pd.read_excel(file_path)

# Проверяем структуру данных
print(df.head())  # Вывод первых строк для проверки

# Шаг 2: Построение графика
plt.figure(figsize=(25, 25))  # Размер окна графика

# Используем данные из DataFrame
plt.plot(df['x'], df['y'], marker='o', label='курс доллара')

# Настройка графика
plt.title('курс доллара')
plt.xlabel('год')
plt.ylabel('цена')
plt.legend()
plt.grid(True)  # Включить сетку

# Шаг 3: Отображаем график
plt.show()