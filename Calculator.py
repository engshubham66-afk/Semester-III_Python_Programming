while True:
 print("\n---MENU---\n")
 print("1. Addition")
 print("2. Substraction")
# print("3. Multiplication")
# print("4. Division")
 print("5. Exit")

 choice = int(input("Enter your choice: "))

 if choice == 1 :
     num1 = int(input("Enter first number: "))
     num2 = int(input("Enter second number: "))
     result = num1 + num2
     print("Sum = "+ str(result))

 elif choice == 2:
     num1 = int(input("Enter first number: "))
     num2 = int(input("Enter second number: "))
     result = num1 - num2
     print("Substraction = "+ str(result))    

 elif choice == 5 :
     print("Program Ended") 
     break
        
 else:
     print("Invalid choiice")    
    
