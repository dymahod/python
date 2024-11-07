import decimal

def compute_pi(digits):
    decimal.getcontext().prec = digits + 2
    pi = decimal.Decimal(0)

    for k in range(digits + 2):
        pi += (decimal.Decimal(-1) ** k) / (decimal.Decimal(2) * decimal.Decimal(k) + decimal.Decimal(1))

    return str(pi)[:digits + 2]

# Пример использования программы
num_digits = int(input("Введите число знаков после запятой, до которого нужно вычислить пи: "))
pi_value = compute_pi(num_digits)
print(f"Число пи до {num_digits} знаков после запятой: {pi_value}")