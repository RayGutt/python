def isWithinHundred(number):
    if abs(1000 - number) <= 100 or abs(2000 - number) <= 100:
        return True
    else:
        return False


while(True):
    number = input("Please type a number (type 'q' to exit): ")
    if number == 'q':
        break
    else:
        result =  isWithinHundred(int(number))
        print(result)

