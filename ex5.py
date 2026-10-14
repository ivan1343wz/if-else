#5
BANKNOTES = (5000, 2000, 1000, 500, 200, 100)

def calculate_banknotes(amount):
    result = {}
    for banknote in BANKNOTES:
        count = amount // banknote
        result[banknote] = count
        amount = amount % banknote
    return result
amount = int(input("введите сумму для снятия: "))
if amount <=0 or amount % 100 != 0:
    print("сумма должна быть положительной и кратной 100")
else:
    banknotes = calculate_banknotes(amount)
    print('отчет о выдаче наличных:')
    for banknote, count in banknotes.items():
        if count > 0:
            print(f"купюр по {banknote} руб: {count}")
    print(f"общая сумма: {amount} руб.")
