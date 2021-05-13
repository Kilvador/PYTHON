#2 Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
seconds = int(input('Введите количество секунд для конвертации: '))
minutes = seconds // 60
hours = minutes // 60
left_seconds = seconds % 60
left_minutes = minutes % 60

s_out = ''
m_out = ''
h_out = ''

if left_seconds < 10:
    s_out = f"0{left_seconds}"
else:
    s_out = left_seconds

if left_minutes < 10:
    m_out = f"0{left_minutes}"
else:
    m_out = left_minutes

if hours < 10:
    h_out = f"0{hours}"
else:
    h_out = hours

print(f"Вы указали такое время (чч:мм:сс): {h_out}:{m_out}:{s_out}")

#EOF