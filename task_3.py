def err():
    print("Input was not an intenger. Try again >:(")
    calculate()
def calculate():
    a = 0
    a = input("Print number to do calculation with: ")
    try:
        a = int(a)
    except:
        err()
    else:
        b = 0
        for i in range(int(a) + 1):
            b = b + i
        print(b)
calculate()

