#1
bid = 0.13
income = float(input("Введите годовой доход в рублях: "))
tax = income * bid
net_income = income - tax
print(f"Общий доход: {income:,.2f}".replace(',', ' '))
print(f"Сумма налога: {tax:,.2f}".replace(',', ' '))
print(f"Доход после вычета налога: {net_income:,.2f}".replace(',', ' '))
