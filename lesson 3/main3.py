number = int(input("Enter a number : "))

if number > 50:
    print(number, "is greater than 50")
    if number % 2 == 0:
        print("and it's even")
    else:
        print("and it's odd")
else:
    print(number, "is less than 50")
    if number % 2 == 0:
        print("and it's even")
    else:
        print("and it's odd")

