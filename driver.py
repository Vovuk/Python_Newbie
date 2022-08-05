speed = int(input("Input speed drive: "))
if speed > 200:
    print("Speed isn't correct!")
else:
    if speed > 60:
        print("Driver violets!")
    else:
        if speed == 0:
            print("The car is standing!")
        else:
            if speed < 0:
                print("Speed isn't correct!")
            else:
                print("Driver not violets")