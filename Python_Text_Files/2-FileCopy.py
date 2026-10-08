try:
    with open(r"C:\\Users\\sande\\Documents\\sh.txt") as f1:
        with open(r"C:\\Users\\sande\\Documents\\A.txt", "w") as f2:
            for i in f1:
                f2.write(i)

except:
    print("file not available. Please create first.")                

else:
    f1.close()
    print("File closed.")

