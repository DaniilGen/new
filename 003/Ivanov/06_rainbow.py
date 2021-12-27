# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код


q = 0
x = 50
y = 50
xx = 350
yy = 450
for i in range( 7 ):
    q = 5
    x += q*i
    y += q*i
    xx += q*i
    yy += q*i
    sd.line( start_point= sd.Point( x, y ), end_point=sd.Point( xx, yy ),  color = rainbow_colors[i], width=4)



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
