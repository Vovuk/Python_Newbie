a = int(input())
if a < 1582:
    print("error")
elif a % 4 == 0 and not (a % 100 == 0 and a % 400 != 0):
    print("366")
else:
    print("365")
