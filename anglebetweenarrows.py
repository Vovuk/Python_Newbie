# Дано значение времени в 12-ти часовом формате h:m:s.
# Определить угол в градусах между положением часовой
# стрелки в начале суток и ее положением в h часов, m минут и s секунд.

h = int(input())
m = int(input())
s = int(input())

if 0 > h or h > 11 or m < 0 or m > 59 or s < 0 or s > 59:
    print('error')
else:
    angelH = 360 / 12
    angelM = angelH/ 60 
    angelS = angelM/ 60
    angel = angelH * h + angelM * m + angelS *s
    print(round(angel, 2))
