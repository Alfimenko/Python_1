def err():
    print("Input was not an intenger. Try again >:(")
    calculate()
def calculate():
    a = input("Print number of hours: ")
    try:
        a = int(a)
    except:
        err()
    else:
        pass
    b = input("Print number of minutes: ")
    try:
        b = int(b)
    except:
        err()
    else:
        pass
    c = input("Print number of seconds: ")
    try:
        c = int(c)
    except:
        err()
    else:
        pass
    print("Sum of th seconds: " + str(a * 3600 + b * 60 + c))
calculate()

