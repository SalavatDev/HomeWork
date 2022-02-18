
# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.


def pers_info(name, surname, birth, city, email, phone):
    return f'Name: {name}; Surname: {surname}; Year of birth: {birth}; City of residence: {city}; Email: {email}; Telephone: {phone}'


my_info = pers_info(surname='Petrov', name='Ivan', email='ggg@mail.ru', birth=2001, city='Moscow', phone='565-255')
print(my_info)

