import numpy as np

arr1 = np.array(list(map(int, input('Enter first ARRAY ELEMENTS: ').split())))
arr2 = np.array(list(map(int, input('Enter second ARRAY ELEMENTS: ').split())))

# part 7(a)
def array_filled_with_1():
    rows = int(input('Enter no. of ROWS: '))
    cols = int(input('Enter no. of COLUMN: '))

    arr = np.ones((rows, cols), dtype = int)
    print("Array filled with 1: \n", arr)

# part 7(b)   Find maximum & minimum value
def maximum_minmum_value()    :
    print('First array: ',arr1)
    print('Maximum value of the first array: ', max(arr1))

    print('Second array: ', arr2)
    print('Minimum value of the second array: ', min(arr2))

# part 7(c) Dot product of arrays

def dot_product_arrays() :
    print('First array: ',arr1)
    print('Second array: ',arr2)
    
    print('Dot product of two arrays: ', arr1 @ arr2)

# part 7(d) Reshape array 1d to 2d

def reshape_1d_to_2d() :
    print('First array: ',arr1)

    newarr = arr1.reshape(2, 2)    
    print('Reshape array of first array: \n', newarr)

def main_menu():
    while True:
        print('\n---MENU---\n')
        print("1. Create an array filled with 1's")    
        print('2. Find maximum and minimum value')
        print('3. Dot product of 2 arrays')
        print('4. Reshape a 1-D to 2-D array')
        print('5. Exit')

        ch = int(input('Enter your choice as natural numbers: '))

        if ch == 1:
            array_filled_with_1()  

        elif ch == 2:
            maximum_minmum_value()

        elif ch == 3:
            dot_product_arrays() 

        elif ch == 4:
            reshape_1d_to_2d()

        elif ch == 5:
            print('Program is ending.')
            break                 

        else:
            print('Invalid choice!')    
            print('Please enter digits (1-5) and try again.')


main_menu()