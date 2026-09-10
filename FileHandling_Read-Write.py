try:
    f=open("D:\\filehandling\\n.txt", "r")
    # f.write("Learn coding\n Shubham | Sandeep")
    print(f.readlines())
except:
    print("file not available.")

