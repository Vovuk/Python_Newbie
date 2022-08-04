a1 = int(input())
a2 = int(input())
a3 = input()

if a3 == '/' and a2 == 0:
    print("Don't divide by zero!")
elif a3 == '/':
    print(a1 / a2)
elif a3 == '+':
    print(a1 + a2)
elif a3 == '-':
    print(a1 - a2)
elif a3 == '*':
    print(a1 * a2)
else:
    print('Fault')
