with open("C:\\Users\\sande\\Documents\\A.txt", "a+") as file:
      file.write("Append at last ")
      file.seek(0)
      content = file.readlines()
      print(content)