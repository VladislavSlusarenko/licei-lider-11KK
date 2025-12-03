bill = float(input("Сума рахунку (грн): "))

tips = bill * 0.10
total = bill + tips
per_person = total / 3

print("Кожен платить:", per_person)