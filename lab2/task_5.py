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
