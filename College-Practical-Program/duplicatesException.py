num_list = list(map(int, input('Enter integer numbers: ').split()))
duplicates = []

try:
    for i in range (len(num_list)):
        if num_list[i] in num_list[i+1:] and num_list[i] not in duplicates:
            duplicates.append(num_list[i])

    if duplicates:
        raise Exception ('Duplicate number found: ' + str(duplicates))
            
    else:
        print('No duplicate number found.')    

except Exception as e:            
    print('Exception: ', e)
