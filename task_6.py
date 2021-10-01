def err():
    print("Input was not an intenger. Try again >:(")
    calculate()
def calculate():
    a = input("Print your number: ")
    try:
        a = int(a)
    except:
        err()
    else:
        pass
    b = 0
    for i in range(len(str(a))):
        b += int(str(a)[i])
    print(b)
calculate()
