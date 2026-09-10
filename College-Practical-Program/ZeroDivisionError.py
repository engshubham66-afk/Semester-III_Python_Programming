a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
try:
    c = a/b
    print("Result: ",c)

except:
    print("Can't divide by zero")
    print('Handle')