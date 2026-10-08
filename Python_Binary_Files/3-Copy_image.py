source_path = r"C:\\Users\\sande\\Pictures\\God images\\taj mahal.jpg"
destination_path = r"C:\\Users\\sande\\Documents\\my-image\\copy taj mahal.jpg"



with open(source_path, "rb") as source:
    image_data = source.read()
    with open(destination_path, "wb") as destination:
        destination.write(image_data)

print("Image copied successfully.")        
print("File size: ", len(image_data), "bytes")