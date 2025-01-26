a = 45
print(a, "type :", type(a))

b = 7.13
print(b, "type :", type(b))

c = "Python"
print(c, "type :", type(c))

d = False
print(d, "type :", type(d))

#Type-casting : Converting one data type into another type
weight = 55.8 #float
weight_int = int(weight)
print(weight_int, "type :", type(weight_int))
number =  4307
number_str = str(number)
print(number_str, "type :", type(number_str))
number_str_float = float(number_str)
print(number_str_float, "type :", type(number_str_float))

#Arithmetic operators
num1 = 40
num2 = 7

print("Addition :", num1 + num2)
print("Subtraction :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division :", num1 / num2)
print("Floor Division :", num1 // num2)
print("Modulus :", num1 % num2)
print("Exponential :", 7 ** 7 )
print("Square Root :", 25 ** 0.5)

#String operations 
firstName = "Vicky"
lastName = "Jang"
print(firstName +" "+ lastName)

text = "Enhypen"
print(text * 7)

word = "Engene"
print("Length of a string :", len(word))
print("First letter :", word[0])
#print("Last letter :", word[5])
print("Last letter :", word[-1])
print("First 3 letters :", word[0:3])
print("Last 3 letters :", word[3:6])
print("Middle 3 letters :", word[1:4])