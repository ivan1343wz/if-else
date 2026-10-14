#1
bid = 0.13
income = float(input("введите годовой доход в рублях "))
tax = income * bid
net_income = income - tax
print(f"общий доход {income:,.2f}".replace(',', ' '))
print(f"сумма налога {tax:,.2f}".replace(',', ' '))
print(f"доход после вычета налога {net_income:,.2f}".replace(',', ' '))
