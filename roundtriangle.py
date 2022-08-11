from math import sqrt


def compute_len(x_0, y_0, x_1, y_1):
    lin_line = sqrt((x_1 - x_0)**2 + (y_1 - y_0)**2)
    return lin_line


x_a = float(input("x_a= "))
y_a = float(input("y_a= "))
x_b = float(input("x_b= "))
y_b = float(input("y_b= "))
x_c = float(input("x_c= "))
y_c = float(input("y_c= "))

c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)

if a + b <= c or b + c <= a or a + c <= b:
    print("Error! Triangel does not exist.")

else:
    p = a + b + c
    p_p = p / 2
    r = sqrt(((p_p - a) * (p_p - b) * (p_p - c)) / p_p)
    s = sqrt((p_p) * (p_p - a) * (p_p - b) * (p_p - c))
    R = (a * b * c) / (4 * s)
    M_a = 1/2*(sqrt(2 * (c**2+b**2) - a**2))
    M_b = 1/2*(sqrt(2 * (a**2+c**2) - b**2))
    M_c = 1/2*(sqrt(2 * (b**2+a**2) - c**2))
    sum = M_a + M_b + M_c

    print("Radius of the inscribed circle: ", round(r, 4))
    print("Radius of the circumscribed circle: ", round(R, 4))
    print("Summary of median: ", round(sum, 4))
