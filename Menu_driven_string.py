s = input("Enter a string: ")

while True:
    print("\n-----nMENU-----\n")
    print("1. Convert to uppercase")
    print("2. Convert to lowercase")
    print("3. Find length of String")
    print("4. Count Occurrences of a character")
    print("5. Replace a word")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      print("Uppercase String: ",s.upper())

    elif choice == 2 :
       print("Lowercase String: ",s.lower())

    elif choice == 3 :
       print("Length of String: ",len(s))   

    elif choice == 4:
       ch = input("Enter character to count: ")
       print("Count Occurrences of a character: ",s.count(ch))   

    elif choice == 5:
       old = input("Enter word to replace: ")
       new = input("Enter new word: ")
       print("Modified String: ", s.replace(old, new))
    elif choice == 6:
       print("Program Ended")
       break
      
    else:
       print("Invalid choice")   
