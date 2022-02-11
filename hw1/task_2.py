
# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

sec = int(input('Enter the time in seconds: '))
hours = sec // 3600
days = hours // 24
hours = hours % 24
minute = (sec % 3600)//60
sec = sec % 60

result = f'{days:02}:{hours:02}:{minute:02}:{sec:02}'
print(result)





