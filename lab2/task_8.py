name = "Торговый центр «Иркутяночка»"
year = 2023
floors = 5
area = 2000
print("=== ПАСПОРТ ОБЪЕКТА ===")
print(f"Название: {name}")
print(f"Год постройки: {year}")
print(f"Этажность: {floors}")
print(f"Площадь: {area:.2f} кв.м")
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
#задание 3
# Входные данные
celsius = 25.0  # можно менять значение
fahrenheit = celsius * 9/5 + 32
# Определение состояния воды
if celsius <= 0:
    state = "Лёд"
elif celsius < 100:
    state = "Жидкость"
else:
    state = "Пар"
# Вывод
print("=== КОНВЕРТЕР ТЕМПЕРАТУР ===")
print(f"{celsius}°C = {fahrenheit:.1f}°F")
print(f"Состояние воды: {state}")
#задание 4
# Входные данные (1-7, где 1 = понедельник)
day_number = 3
days = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}

work_mode = {
    1: "10:00 - начало смены",
    2: "10:00 - начало смены",
    3: "10:00 - начало смены",
    4: "10:00 - начало смены",
    5: "10:00 - начало смены",
    6: "Отдых",
    7: "Отдых"
}

# Проверка и вывод
if 1 <= day_number <= 7:
    print("=== РАБОЧИЙ ГРАФИК ===")
    print(f"День: {days[day_number]}")
    print(f"Режим: {work_mode[day_number]}")
else:
    print("Ошибка: номер дня должен быть от 1 до 7")
#задание 5
price_per_item = 150.0   
quantity = 40  
total = price_per_item * quantity
if total < 1000:
    discount_rate = 0
    discount_name = "0%"
elif total <= 5000:
    discount_rate = 0.05
    discount_name = "5%"
else:
    discount_rate = 0.10
    discount_name = "10%"

discount_amount = total * discount_rate
final_total = total - discount_amount   
print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Цена за единицу: {price_per_item:.2f} руб")
print(f"Количество: {quantity}")
print(f"Сумма без скидки: {total:.2f} руб")
print(f"Скидка: {discount_name}")
print(f"Сумма скидки: {discount_amount:.2f} руб")
print(f"Итого к оплате: {final_total:.2f} руб") 

#задание 6
materials = ["Кирпич", "Цемент", "Песок", "Арматура", "Бетон"]

print("=== КАТАЛОГ МАТЕРИАЛОВ ===")
print(f"Исходный список: {materials}")
print(f"\nПервый элемент: {materials[0]}")
print(f"Последний элемент: {materials[-1]}")
print(f"Средние элементы: {materials[2]}")
materials.append("Доски")
materials.append("Гвозди")
print(f"\nПосле добавления: {materials}")
removed = materials.pop(1)
print(f"Удалён элемент: {removed}")
print(f"\nИтоговый список: {materials}")
print(f"Длина списка: {len(materials)}")

#задание 7
prices = {
    "Кирпич": 12.50,
    "Цемент": 450.00,
    "Песок": 800.00,
    "Арматура": 48000.00,
    "Бетон": 4200.00

}
print("=== ПРАЙС-ЛИСТ ===")
print(f"Исходный словарь: {prices}")
prices["Доски"] = 1500.00
prices["Гвозди"] = 89.50
print(f"\nПосле добавления: {prices}")
old_price = prices["Цемент"]
prices["Цемент"] = round(prices["Цемент"] * 1.10, 2)
print(f"\nЦемент: {old_price} → {prices['Цемент']} (+10%)")
removed = prices.pop("Песок")
print(f"Удалён материал: Песок (цена {removed})")
avg_price = sum(prices.values()) / len(prices)
print(f"\nСредняя цена: {avg_price:.2f} руб")
print(f"\nИтоговый прайс-лист: {prices}")

#задание 8
supplier1 = ["Кирпич", "Цемент", "Песок", "Арматура"]
supplier2 = ["Цемент", "Бетон", "Арматура", "Доски"]
supplier3 = ["Кирпич", "Арматура", "Бетон", "Гвозди"]
set1 = set(supplier1)
set2 = set(supplier2)
set3 = set(supplier3)
print("=== АНАЛИЗ ЗАКАЗОВ ===")
print(f"Подрядчик 1: {supplier1}")
print(f"Подрядчик 2: {supplier2}")
print(f"Подрядчик 3: {supplier3}")
all_materials = set1 | set2 | set3
print(f"\nВсе уникальные материалы: {sorted(all_materials)}")
common_all = set1 & set2 & set3
print(f"Общие для всех: {common_all}")
only_first = set1 - set2 - set3
print(f"Только у подрядчика 1: {only_first}")
exactly_two = (set1 & set2) | (set1 & set3) | (set2 & set3)
exactly_two = exactly_two - common_all
print(f"Ровно у двух подрядчиков: {sorted(exactly_two)}")

#задание 9
import re
addresses = [
    "  г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100  "
]
def clean_address(address):
    """Очистка и форматирование адреса"""
    address = address.strip()
    address = re.sub(r'(г\.)([А-Я])', r'\1 \2', address)
    address = re.sub(r'(ул\.)([А-Я])', r'\1 \2', address)
    address = re.sub(r'(д\.)(\d)', r'\1 \2', address)
    address = re.sub(r',([А-Яа-я])', r', \1', address)
    address = re.sub(r'\s+', ' ', address)
    
    return address
print("=== ОЧИСТКА АДРЕСОВ ===\n")
for i, addr in enumerate(addresses, 1):
    cleaned = clean_address(addr)
    print(f"#{i}")
    print(f"ДО: '{addr}'")
    print(f"ПОСЛЕ: '{cleaned}'\n")
    #задание 10
warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

print("=== СИСТЕМА УЧЁТА СКЛАДА ===\n")
print(f"{'Материал':<12} {'Кол-во':<8} {'Цена':<10} {'Мин.':<8} {'Стоимость':<12}")
print("-" * 55)
critical_list = []
total_cost = 0
max_cost = 0
most_expensive = ""

for name, data in warehouse.items():
    qty = data["quantity"]
    price = data["price"]
    min_qty = data["min_quantity"]
    cost = qty * price
    total_cost += cost
    
    if cost > max_cost:
        max_cost = cost
        most_expensive = name
    
    critical_mark = " КРИТИЧ!" if qty < min_qty else ""
    print(f"{name:<12} {qty:<8} {price:<10.2f} {min_qty:<8} {cost:<12.2f}{critical_mark}")
    
    if qty < min_qty:
        critical_list.append(f"{name}: {qty} < {min_qty}")

print(f"\nОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб")
print(f"Самый дорогой: {most_expensive} ({max_cost:.2f} руб)")

if critical_list:
    print(f"\n⚠️ КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_list)}):")
    for item in critical_list:
        print(f"   - {item}")
else:
    print("\n✅ Критических остатков нет")

# Выдача материала со склада
material_to_issue = "Цемент"
issue_qty = 25

if material_to_issue in warehouse:
    old_qty = warehouse[material_to_issue]["quantity"]
    if old_qty >= issue_qty:
        warehouse[material_to_issue]["quantity"] -= issue_qty
        new_qty = warehouse[material_to_issue]["quantity"]
        print(f"\n=== ВЫДАЧА МАТЕРИАЛА ===")
        print(f"✓ Выдано {issue_qty} единиц '{material_to_issue}'")
        print(f"  Остаток: {old_qty} → {new_qty}")
    else:
        print(f"\nОшибка: недостаточно '{material_to_issue}' (есть {old_qty}, нужно {issue_qty})")
else:
    print(f"\nОшибка: материал '{material_to_issue}' не найден")