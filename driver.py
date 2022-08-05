speed = int(input("Input speed drive: "))
if speed > 200:
    print("Speed isn't correct!")
elif (speed > 60):
    print("Driver violets!")
elif (speed == 0):
    print("The car is standing!")
elif (speed < 0):
    print("Speed isn't correct!")
else:
    print("Driver not violets")