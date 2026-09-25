import sys

print("Program name: ",sys.argv[0])
print("Arguments: ", sys.argv[1:])

n = int(input("Enter the number of ARGUMENTS: "))

try:
    for i in range (1, n + 1):
      print(f"Argument {i}: ", sys.argv[i])

except IndexError:
   print("The number of arguments entered is greater than the arguments provided.")      

