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
