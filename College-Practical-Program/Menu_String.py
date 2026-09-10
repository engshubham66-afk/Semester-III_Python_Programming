sentence = input('Enter a sentence: ')

def freq_character():
    
    ch = input('Enter a character to find frequency: ')
        
    print(f'freqency of a character {ch}: ', sentence.count(ch))

def replace_char()    :
    old_char = input('Enter a word to be replaced: ')
    new_char = input('Enter a chacter by replace: ')
    print('a character to replace by another character: ', sentence.replace(old_char, new_char))

def remove_first_char():
    rch = input(f'Enter a character to remove from ({sentence}): ')
    print(f'After removing the First occurence of character {rch}: ', sentence.replace(rch, '', 1))        

def remove_all_char()    :
    rach = input('Enter a character to remove all occurrence: ')
    print('After removing all characters: ', sentence.replace(rach, ''))


while True:
    print('1. Frequency of a character')    
    print('2. Replace a character by another character')
    print('3. Remove the first occurrence character')
    print('4. Remove all occurrence charaters')
    print('5. exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        freq_character()

    elif choice == 2:   
        replace_char()  
    elif choice == 3:
        remove_first_char() 

    elif choice == 4:
        remove_all_char()

    elif choice == 5:
        print('Ending Program.') 
        exit()
    

    else:
        print('Invalid choice!')   

               



       
 
