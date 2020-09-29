# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = str(input("Введите целое число, с которым будем извращаться (n)"))
number1 = n
number2 = n*2
number3 = n*3

result = int(number1) + int(number2) + int(number3)
print("Сумма чисел n + nn + nnn будет равна", result)
