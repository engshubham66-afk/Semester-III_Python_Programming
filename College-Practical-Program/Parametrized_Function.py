def function_parametrized(n):
       if n % 2 == 0 :
        return True
       else:
          return False  
n = int(input("Enter a number: "))
if function_parametrized(n):
    print("The number is even")
else:    print("The number is odd")    