data = b"hello"

with open("data.bin", "rb") as file:
    content = file.read()
    print(content)