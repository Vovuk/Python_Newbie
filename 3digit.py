number = int(input("Input number: "))
strnumber = str(number)
if len(strnumber) <= 2:
    print("Third digit is missing ")
else:
    print("Third digit is " + strnumber[2])
