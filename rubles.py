k = int(input())

if k not in range(1, 100):
    print('ошибка')
else:
    if k not in [11, 12, 13, 14] and k % 10 == 1:
        print(k, 'рубль')
    elif k not in [11, 12, 13, 14] and k % 10 in [2, 3, 4]:
        print(k, 'рубля')
    else:
        print(k, 'рублей')