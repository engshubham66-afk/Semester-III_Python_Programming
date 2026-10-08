
source_path = r"C:\\Users\\sande\\Pictures\\God images\\taj mahal.jpg"
destination_path = r"C:\\Users\\sande\\Documents\\my-image\\copy taj mahal.jpg"

with open(source_path, "rb") as source:
    image_data = source.read()

print("Source file size:", len(image_data), "bytes")
print("First 10 bytes:", image_data[:10])

with open(destination_path, "wb") as destination:
    destination.write(image_data)

with open(destination_path, "rb") as destination:
    copied_data = destination.read()

print("Copied file size:", len(copied_data), "bytes")
print("Files identical:", image_data == copied_data)