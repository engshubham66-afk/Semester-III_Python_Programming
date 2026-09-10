# i = 1 
# while i <= 5:
#     print(i)
#     i = i + 1
    
# print("Done")

# guess game
secret_number = 7
count = 0
limit = 3
while count < limit:
    Guess = int(input(('Guess: ')))
    count =+ 1
    if Guess == secret_number:
        print('you won')
        break
else:
    print("Sorry, you failed")
    

result = 24.738886
result1 = round(result, 2)