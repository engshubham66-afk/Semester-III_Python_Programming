import random

while True:
    ch = input("Do you want to roll dice ? (y / n) ").lower()
    if ch == "y":
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print(f"Dice roll is {roll1, roll2}")

    elif ch == 'n' :
        print("Thank you for playing game!")
        break

    else: 
        print("Invalid choice!")
    
   



    