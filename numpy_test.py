import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("NumPy is working!")
print(arr)
print(type(arr))
print("Dimension is: ", arr.ndim)
print(np.__version__)

# 2d array
arr = np.array([[12, 13, 14], [10, 11, 14]])
print(arr)
print(type(arr))
print("Dimension is: ", arr.ndim)

def create_array_of_ones():
   # create an array with 1's
 
   rows = int(input("Enter no. of rows: "))
   cols = int(input("Enter no. of column: "))

   arr = np.ones((rows, cols), dtype = int)

   print("\nArray filled with 1s: \n", arr)

def main_menu() :
    while True:
        print("\n--- MENU --- ")
        print("1. Create an array filled with 1's")
        print("2. exit")

        ch = int(input("Choose an option (1-2): "))

        if ch == 1 :
            create_array_of_ones()
        elif ch == 2 :
            print("Exiting program.")    
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
if __name__ == "__main__":
   main_menu()