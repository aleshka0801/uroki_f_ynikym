import matplotlib.pyplot as plt
# данные для диаграммы
categories = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
values = [7, 9, 11, 4, 8]

# создание столбчатой диаграммы
plt.bar(categories, values)

# добавление заголовка и подписей к осям
plt.title('температура на недели')
plt.xlabel('дни недели')
plt.ylabel('t воздуха')

# отображение диаграммы
plt.show()