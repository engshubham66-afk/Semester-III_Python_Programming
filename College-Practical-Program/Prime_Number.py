num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number.")

else:
    
    for i in range(0, num):
        i = 2
        if (num % i == 0):
            print(f"{num} is not a prime number.")    
            exit()

    else:
        print(f"{num} is a prime number.")   