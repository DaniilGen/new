#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
<<<<<<< HEAD
<<<<<<< HEAD
print(round(3.1415926 * (radius ** 2), 4))
=======
square = round(3.1415926 * (radius ** 2), 4)
print(square)

>>>>>>> 341e0f52f6cc9049d8719f58db8a521275f5857a
=======
square = round(3.1415926 * (radius ** 2), 4)
print(square)

=======
print(round(3.1415926 * (radius ** 2), 4))
>>>>>>> 12eef8ccb11bebf8d2c24e207d99da6575481a28
>>>>>>> 9e4ea4dcc8a4f845909ef8fcd064ff92e9055da8


# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
x, y = point
<<<<<<< HEAD
<<<<<<< HEAD
if ((x ** 2 + y ** 2) ** 0.5) <= radius:
=======
if((x ** 2 + y ** 2) ** 0.5) <= radius:
>>>>>>> 341e0f52f6cc9049d8719f58db8a521275f5857a
=======
if((x ** 2 + y ** 2) ** 0.5) <= radius:
=======
if ((x ** 2 + y ** 2) ** 0.5) <= radius:
>>>>>>> 12eef8ccb11bebf8d2c24e207d99da6575481a28
>>>>>>> 9e4ea4dcc8a4f845909ef8fcd064ff92e9055da8
    print(True)
else:
    print(False)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
x, y = point_2
<<<<<<< HEAD
<<<<<<< HEAD
if ((x ** 2 + y ** 2) ** 0.5) <= radius:
=======
if((x ** 2 + y ** 2) ** 0.5) <= radius:
>>>>>>> 341e0f52f6cc9049d8719f58db8a521275f5857a
=======
if((x ** 2 + y ** 2) ** 0.5) <= radius:
=======
if ((x ** 2 + y ** 2) ** 0.5) <= radius:
>>>>>>> 12eef8ccb11bebf8d2c24e207d99da6575481a28
>>>>>>> 9e4ea4dcc8a4f845909ef8fcd064ff92e9055da8
    print(True)
else:
    print(False)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False
<<<<<<< HEAD
<<<<<<< HEAD


=======
>>>>>>> 341e0f52f6cc9049d8719f58db8a521275f5857a
=======
=======


>>>>>>> 12eef8ccb11bebf8d2c24e207d99da6575481a28
>>>>>>> 9e4ea4dcc8a4f845909ef8fcd064ff92e9055da8
