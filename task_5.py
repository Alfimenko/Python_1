def err():
    print("Input was not a number. Try again >:(")
    calculate()
def calculate():
    a = input("Print your mass: ")
    try:
        a = float(a)
    except:
        err()
    else:
        pass
    b = input("Print your heght: ")
    try:
        b = int(b)
    except:
        err()
    else:
        pass
    print("Your BMI is " + str(a / b * b))
calculate()

