import math
a = float(input())
b = float(input())
v = int(input())
if a <= 0 or b <= 0 or v <= 0:
    print("error")
else:
    s = a **2 * 5
    c = s * b /1000
    d = c / v
    print(math.ceil(d))