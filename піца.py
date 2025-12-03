qty = int(input("Скільки піц бажаєте замовити? "))
price = float(input("Ціна однієї піци: "))

total = qty * price
total_with_discount = total * 0.9

print("Підсумкова вартість:", total_with_discount)