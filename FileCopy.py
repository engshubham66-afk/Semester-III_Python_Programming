try:
    with open("D:\\filehandling\\A.txt") as f2:
        with open("D:\\filehandling\\C.txt", "w") as f3:
            for i in f2:
                f3.write(i)

except:
    print("file not available. Please create first.")                

else:
    f2.close()
    print("File closed.")

