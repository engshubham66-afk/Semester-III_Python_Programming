First_string = input('Enter FIRST STRING: ')
Second_string = input('Enter SECOND STRING to find index in the FIRST STRING: ')

index_list = []
start = 0

while True:
    pos = First_string.find(Second_string, start)

    if pos == -1:
        break
        
    index_list.append(pos)
    start = pos + 1
        

if len(index_list) == 0:
    print('index: -1')

else :
    print('index: ',index_list)    
    