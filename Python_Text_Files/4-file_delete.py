import os 
if os.path.exists("D:\\filehandling\\A.txt"):
    os.remove("D:\\filehandling\\A.txt")
    print("File deleted successfully.")    
else:
    print("File not available.")    

