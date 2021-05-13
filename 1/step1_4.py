#4 Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

while True:
    number = float(input('Введите число: '))
    if number < 0:
        print('Число не положительное!')
        continue
    elif (number).is_integer() == False:
        print('Число не целое!')
        continue
    else:
        break
number = int(number)

max = number % 10
left = number // 10

while left > 0:
    if left % 10 > max:
        max = left % 10
    left = left // 10

print(f'Вы ввели: {number}, максимальная цифра: {max}')
