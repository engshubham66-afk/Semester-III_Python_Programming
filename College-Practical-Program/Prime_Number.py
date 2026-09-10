n = int(input("Enter a number: "))
if n < 2:
    print("Not Prime Number") 
else:  
   i=2
while i <= n/2:
     if n % i == 0:
       print("Not Prime number")
       break
     i = i + 1
else:
    print("It is a prime number.")