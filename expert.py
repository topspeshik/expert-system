import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

df = pd.read_csv('forecast_2023-06-22T02.37_58.978Z.csv', sep=',')

root = tk.Tk()
root.title('График суммы значений')

# Создание вкладок
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10)

frame = ttk.Frame(root)
notebook.add(frame, text='График')

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

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
df['Ветер:А'] = (df['Ветер:А'] * 7) / 9


def update_plot():
    df_modified = df.copy()
    try:
        df_modified['Ветер:А'] *= float(wind_spinbox.get())
        df_modified['Солнце'] *= float(sun_spinbox.get())
        df_modified['Больницы'] *= float(health_spinbox.get())
        df_modified['Заводы'] *= float(factory_spinbox.get())
        df_modified['Дома А'] *= float(home_spinbox.get())
    except:
        pass
    df_modified['Ветер+Солнце'] = df_modified['Ветер:А'] + df_modified['Солнце']
    df_modified['Больницы+Заводы+Дома А'] = df_modified['Больницы'] + df_modified['Заводы'] + df_modified['Дома А']


    ax.clear()

    ax.plot(df_modified.index, df_modified['Ветер+Солнце'], label='Ветер+Солнце')
    ax.plot(df_modified.index, df_modified['Больницы+Заводы+Дома А'], label='Больницы+Заводы+Дома А')

    ax.set_title('График суммы значений')
    ax.set_xlabel('Индекс')
    ax.set_ylabel('Сумма значений')
    ax.legend()

    canvas.draw()

update_button = ttk.Button(frame, text='Обновить график', command=update_plot)
update_button.grid(row=5, column=0, columnspan=2, pady=10)

update_plot()

frame2 = ttk.Frame(notebook)
notebook.add(frame2, text='Расчеты')

# Элементы управления для ввода значений и их стоимостей
objects_and_costs = {
    'Дома А': {'quantity_spinbox': None, 'cost_entry': None},
    'Заводы': {'quantity_spinbox': None, 'cost_entry': None},
    'Больницы': {'quantity_spinbox': None, 'cost_entry': None},
    'Ветер:А': {'quantity_spinbox': None, 'cost_entry': None},
    'Солнце': {'quantity_spinbox': None, 'cost_entry': None},
}

row_counter = 0
# Дома
label_quantity_homes = ttk.Label(frame2, text='Количество Домов:')
objects_and_costs['Дома А']['quantity_spinbox']  = ttk.Spinbox(frame2, from_=1, to=10)
label_quantity_homes.grid(row=row_counter, column=0, padx=10, pady=10)
objects_and_costs['Дома А']['quantity_spinbox'] .grid(row=row_counter, column=1, padx=10, pady=10)

label_cost_homes = ttk.Label(frame2, text='Цена Домов за 1 МВт:')
objects_and_costs['Дома А']['cost_entry']  = ttk.Entry(frame2)
label_cost_homes.grid(row=row_counter, column=2, padx=10, pady=10)
objects_and_costs['Дома А']['cost_entry'] .grid(row=row_counter, column=3, padx=10, pady=10)

row_counter += 1

# Заводы
label_quantity_factories = ttk.Label(frame2, text='Количество Заводов:')
objects_and_costs['Заводы']['quantity_spinbox']  = ttk.Spinbox(frame2, from_=1, to=10)
label_quantity_factories.grid(row=row_counter, column=0, padx=10, pady=10)
objects_and_costs['Заводы']['quantity_spinbox'] .grid(row=row_counter, column=1, padx=10, pady=10)

label_cost_factories = ttk.Label(frame2, text='Цена Заводов за 1 МВт:')
objects_and_costs['Заводы']['cost_entry']  = ttk.Entry(frame2)
label_cost_factories.grid(row=row_counter, column=2, padx=10, pady=10)
objects_and_costs['Заводы']['cost_entry'] .grid(row=row_counter, column=3, padx=10, pady=10)

row_counter += 1

# Больницы
label_quantity_hospitals = ttk.Label(frame2, text='Количество Больниц:')
objects_and_costs['Больницы']['quantity_spinbox']  = ttk.Spinbox(frame2, from_=1, to=10)
label_quantity_hospitals.grid(row=row_counter, column=0, padx=10, pady=10)
objects_and_costs['Больницы']['quantity_spinbox'] .grid(row=row_counter, column=1, padx=10, pady=10)

label_cost_hospitals = ttk.Label(frame2, text='Цена Больниц за 1 МВт:')
objects_and_costs['Больницы']['cost_entry']  = ttk.Entry(frame2)
label_cost_hospitals.grid(row=row_counter, column=2, padx=10, pady=10)
objects_and_costs['Больницы']['cost_entry'] .grid(row=row_counter, column=3, padx=10, pady=10)

row_counter += 1

# Ветряки
label_quantity_windmills = ttk.Label(frame2, text='Количество Ветряков:')
objects_and_costs['Ветер:А']['quantity_spinbox']  = ttk.Spinbox(frame2, from_=1, to=10)
label_quantity_windmills.grid(row=row_counter, column=0, padx=10, pady=10)
objects_and_costs['Ветер:А']['quantity_spinbox'] .grid(row=row_counter, column=1, padx=10, pady=10)

label_cost_windmills = ttk.Label(frame2, text='Цена Ветряков за 1 МВт:')
objects_and_costs['Ветер:А']['cost_entry']  = ttk.Entry(frame2)
label_cost_windmills.grid(row=row_counter, column=2, padx=10, pady=10)
objects_and_costs['Ветер:А']['cost_entry'] .grid(row=row_counter, column=3, padx=10, pady=10)

row_counter += 1

# Солнечные панели
label_quantity_solarpanels = ttk.Label(frame2, text='Количество Солнечных панелей:')
objects_and_costs['Солнце']['quantity_spinbox']  = ttk.Spinbox(frame2, from_=1, to=10)
label_quantity_solarpanels.grid(row=row_counter, column=0, padx=10, pady=10)
objects_and_costs['Солнце']['quantity_spinbox'] .grid(row=row_counter, column=1, padx=10, pady=10)

label_cost_solarpanels = ttk.Label(frame2, text='Цена Солнечных панелей за 1 МВт:')
objects_and_costs['Солнце']['cost_entry']  = ttk.Entry(frame2)
label_cost_solarpanels.grid(row=row_counter, column=2, padx=10, pady=10)
objects_and_costs['Солнце']['cost_entry'] .grid(row=row_counter, column=3, padx=10, pady=10)

row_counter += 1

# Элементы управления для отображения результатов
result_label = ttk.Label(frame2, text='Результаты расчетов:')
result_label.grid(row=row_counter, column=0, padx=10, pady=10)

result_text = tk.Text(frame2, height=5, width=50)
result_text.grid(row=row_counter + 1, column=0, columnspan=4, padx=10, pady=10)


def calculate_results():
    try:
        # Получение значений из элементов управления и их стоимостей
        total_cost = 0
        total_energy = 0
        num_homes = float(objects_and_costs['Дома А']['quantity_spinbox'].get())
        cost_per_megawatt_homes = float(objects_and_costs['Дома А']['cost_entry'].get())
        total_cost_homes = num_homes * cost_per_megawatt_homes * len(df['Дома А'])
        total_energy_homes = num_homes * df['Дома А'].sum()

        # Заводы
        num_factories = float(objects_and_costs['Заводы']['quantity_spinbox'].get())
        cost_per_megawatt_factories = float(objects_and_costs['Заводы']['cost_entry'].get())
        total_cost_factories = num_factories * cost_per_megawatt_factories * len(df['Заводы'])
        total_energy_factories = num_factories * df['Заводы'].sum()

        # Больницы
        num_hospitals = float(objects_and_costs['Больницы']['quantity_spinbox'].get())
        cost_per_megawatt_hospitals = float(objects_and_costs['Больницы']['cost_entry'].get())
        total_cost_hospitals = num_hospitals * cost_per_megawatt_hospitals * len(df['Больницы'])
        total_energy_hospitals = num_hospitals * df['Больницы'].sum()

        # Ветряки
        num_windmills = float(objects_and_costs['Ветер:А']['quantity_spinbox'].get())
        cost_per_megawatt_windmills = float(objects_and_costs['Ветер:А']['cost_entry'].get())
        total_cost_windmills = num_windmills * cost_per_megawatt_windmills* len(df['Ветер:А'])
        total_energy_windmills = num_windmills * df['Ветер:А'].sum()

        # Солнечные панели
        num_solarpanels = float(objects_and_costs['Солнце']['quantity_spinbox'].get())
        cost_per_megawatt_solarpanels = float(objects_and_costs['Солнце']['cost_entry'].get())
        total_cost_solarpanels = num_solarpanels * cost_per_megawatt_solarpanels* len(df['Солнце'])
        total_energy_solarpanels = num_solarpanels * df['Солнце'].sum()

        # Общие расчеты
        total_cost = total_cost_homes + total_cost_factories + total_cost_hospitals - total_cost_windmills - total_cost_solarpanels
        total_energy = total_energy_homes + total_energy_factories + total_energy_hospitals

        # Расчеты
        total_forecast_energy = total_energy_solarpanels + total_energy_windmills
        total_consumption_energy = total_energy

        remaining_energy = total_forecast_energy - total_consumption_energy

        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f'Остаток энергии: {remaining_energy} МВт\n')
        result_text.insert(tk.END, f'Запас монет: {total_cost} монет\n')

        # Рассчитайте, сколько еще можно купить объектов, и выведите результат в result_text
    except ValueError:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, 'Пожалуйста, введите числовые значения для всех полей.')


calculate_button = ttk.Button(frame2, text='Рассчитать', command=calculate_results)
calculate_button.grid(row=row_counter + 2, column=0, columnspan=4, pady=10)
notebook.add(frame2, text='Рассчет')
root.mainloop()