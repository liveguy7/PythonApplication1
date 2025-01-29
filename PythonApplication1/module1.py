

def averageNumbers():
    num = int(input("Enter numbers "))
    total = 0
    for n in range(num):
        numbers = float(input("Enter a number "))
        total = total + numbers
    avg = total / num

    print("The average is {0}".format(avg))

