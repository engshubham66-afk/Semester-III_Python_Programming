print("Shubham Kumar")


first_name = 'Shubham'
is_online = False
print(first_name)

name = input("What is your name? ")
print("Hello " + name + " !")

birth_year = input("Enter your birth year: ")
age = 2026 - int(birth_year)
print(age)

first_number = input("First number: ")
second_number = input("Second number: ")
sum = int(first_number) + int(second_number)
print("sum: " + str(sum))

course = 'python for Beginners'
print( course.upper() )

print(course.find('for'))
print( course.replace('for', str(7)))
print( course.replace('x', str(7)))

print(10 + 3 * 2)

array = [5,7,9,1,6,8]
print(5 in array)

price = 25
print(price > 10 or price < 30)

temperature = 5

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's a cold")
    print("Done")

weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper( ) == "K":
    converted = weight / 0.45
    print("Weight in Lbs: "+ str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: "+ str(converted))


i = 10
while i >= 0:
    print(i * '*')
    i = i - 1