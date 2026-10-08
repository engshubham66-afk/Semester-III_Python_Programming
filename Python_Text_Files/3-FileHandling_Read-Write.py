try:
    f=open("Shubham.txt", "r+")
    print("Read all lines are ", f.readlines())
    f.write(" using writing mode\n")

except:
    print("file not available.")

