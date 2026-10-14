USD_TO_RUB = 85.12

def convert_usd_to_rub(amount_usd):
    return amount_usd * USD_TO_RUB
usd = float(input("введите сумму в долларах"))
rub = convert_usd_to_rub(usd)
print(f"сумма в рублях: {rub:.2f} руб.")
