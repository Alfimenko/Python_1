print("Calculate area of the room in square meters")
def askInput():
    a = input("Width of the room in meters: ")
    try:
        a = float(a)
    except:
        err()
    else:
        pass
    b = input("Length of the room in meters: ")
    try:
        b = float(b)
    except:
        err()
    else:
        pass
    calcualte(a, b)

def calcualte(a, b):
    print("Correct value types")
    print("Calculating...")
    print("Area of the room is " + str(a * b) + " meters squared")

def err():
    print("One of the two values were not numbers. Try again >:(")
    askInput()
askInput()
