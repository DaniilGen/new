# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
database = (31,28,31,30,31,30,31,31,30,31,30,31)
try:
        month = int(user_input)
except ValueError as e:
	print("Ошибка: Вы ввели не число")
	exit(1)
if month < 0:
	import warnings as w
	w.warn("Индекс введенного месяца меньше нуля")

try:
	answer = database[month-1]
except IndexError as e:
	print("Ошибка: месяца с таким номером не существует")
	exit(2)

print(f"Вы ввели {month} в нем {answer} дней")

