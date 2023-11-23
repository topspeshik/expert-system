import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Загрузка данных из CSV файла
df = pd.read_csv('forecast_2023-06-22T02.37_58.978Z.csv', sep=',')

# Создание главного окна Tkinter
root = tk.Tk()
root.title('График суммы значений')

# Создание фрейма для отображения графика
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Создание выпадающего списка для выбора количества объектов
wind_label = ttk.Label(frame, text='Количество объектов для Ветра:')
wind_spinbox = ttk.Spinbox(frame, from_=1, to=10)
wind_label.grid(row=0, column=0, padx=10, pady=10)
wind_spinbox.grid(row=0, column=1, padx=10, pady=10)

sun_label = ttk.Label(frame, text='Количество объектов для Солнца:')
sun_spinbox = ttk.Spinbox(frame, from_=1, to=10)
sun_label.grid(row=1, column=0, padx=10, pady=10)
sun_spinbox.grid(row=1, column=1, padx=10, pady=10)

health_label = ttk.Label(frame, text='Количество объектов для Больниц:')
health_spinbox = ttk.Spinbox(frame, from_=1, to=10)
health_label.grid(row=2, column=0, padx=10, pady=10)
health_spinbox.grid(row=2, column=1, padx=10, pady=10)

factory_label = ttk.Label(frame, text='Количество объектов для Заводов:')
factory_spinbox = ttk.Spinbox(frame, from_=1, to=10)
factory_label.grid(row=3, column=0, padx=10, pady=10)
factory_spinbox.grid(row=3, column=1, padx=10, pady=10)

home_label = ttk.Label(frame, text='Количество объектов для Домов:')
home_spinbox = ttk.Spinbox(frame, from_=1, to=10)
home_label.grid(row=4, column=0, padx=10, pady=10)
home_spinbox.grid(row=4, column=1, padx=10, pady=10)

# Создание объекта FigureCanvasTkAgg
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Функция для обновления графика при выборе количества объектов
def update_plot():
    # Умножение значений в строках на количество объектов
    df_modified = df.copy()
    try:
        df_modified['Ветер:А'] *= float(wind_spinbox.get())
        df_modified['Солнце'] *= float(sun_spinbox.get())
        df_modified['Больницы'] *= float(health_spinbox.get())
        df_modified['Заводы'] *= float(factory_spinbox.get())
        df_modified['Дома А'] *= float(home_spinbox.get())
    except:
        pass
    # Создание суммированных столбцов
    df_modified['Ветер+Солнце'] = df_modified['Ветер:А'] + df_modified['Солнце']
    df_modified['Больницы+Заводы+Дома А'] = df_modified['Больницы'] + df_modified['Заводы'] + df_modified['Дома А']

    # Очистка графика
    ax.clear()

    # Построение графика
    ax.plot(df_modified.index, df_modified['Ветер+Солнце'], label='Ветер+Солнце')
    ax.plot(df_modified.index, df_modified['Больницы+Заводы+Дома А'], label='Больницы+Заводы+Дома А')

    # Настройка графика
    ax.set_title('График суммы значений')
    ax.set_xlabel('Индекс')
    ax.set_ylabel('Сумма значений')
    ax.legend()
    
    # Обновление canvas
    canvas.draw()

# Кнопка для обновления графика
update_button = ttk.Button(frame, text='Обновить график', command=update_plot)
update_button.grid(row=5, column=0, columnspan=2, pady=10)

# Инициализация первого графика
update_plot()

# Запуск главного цикла Tkinter
root.mainloop()