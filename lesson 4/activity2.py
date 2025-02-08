# without recursion
def find_factorial(num):
    prod = 1
    while num > 0:
        prod = prod * num
        num = num - 1
    return prod


num = int(input("Give me a number : "))
print(find_factorial(num))

print("======================================")
#with recursion
def rec_find_factorial(num):
    if num <= 0:
        return 1
    return num * rec_find_factorial(num-1)


num = int(input("Give me a number : "))
print(rec_find_factorial(num))