firstnumber = int(input("Input first number: "))
secondnumber = int(input("Input second number: "))
thirdnumber = int(input("Input third number: "))
if (firstnumber >= secondnumber and firstnumber >= thirdnumber):
    print("Max number: ", firstnumber)
elif (secondnumber >= firstnumber and secondnumber >= thirdnumber):
    print("Max number: ", secondnumber)
else:
    print("Max number: ", thirdnumber)