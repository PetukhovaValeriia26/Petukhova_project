#задание 2
length = 6.0   # м
width = 4.0    # м
height = 2.8   # м
price_per_sqm = 125.0  # руб/м²

# Расчёты
floor_area = length * width
wall_area = 2 * (length + width) * height
volume = length * width * height
painting_cost = wall_area * price_per_sqm

# Округление до 2 знаков
floor_area = round(floor_area, 2)
wall_area = round(wall_area, 2)
volume = round(volume, 2)
painting_cost = round(painting_cost, 2)

# Вывод
print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Площадь пола: {floor_area} м²")
print(f"Площадь стен: {wall_area} м²")
print(f"Объём помещения: {volume} м³")
print(f"Стоимость покраски стен: {painting_cost} руб")
