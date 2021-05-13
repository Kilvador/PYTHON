#3 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

number = str(input('Введите число: '))
double_n = int(number + number)
number = int(number)
sum = number + double_n
number = str(number)
double_n = str(double_n)
triple_n = int(double_n + number)
sum = sum + triple_n

print(f'Сумма {number} + {double_n} + {triple_n} = {sum}')

#EOF
