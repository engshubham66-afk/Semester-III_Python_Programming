# split the string
arn = "shubham/Rohit"
arn1= arn.split("/")
print(arn1[1])

name = "Shubham Kumar"
print(name.split()," ")

# conversion string into lowercase and uppercase
name = "abhishek"
print(name.upper())
print(name.lower())

# concatenation the string
str1 = "Hello"
str2 = " World"
str = str1 + str2
print(str)

# calculate string length
length = len(str1)
print("Length of the string 'str1' = " , length)

length = len(str2)
print("Length of the string 'str2' = " , length)

length = len(str)
print("Length of the string 'str' = " , length)

# integer variables
num1 = 12
num2 = 5

# integer manipulation
result = num1 / num2
print("Integer division: ",result)

result = num1 * num2
print("Integer multiplication: ",result)

result = num1 + num2
print("Integer addition: ",result)

result = num1 - num2
print("Integer subtraction: ",result)

result = num1 % num2
print("Integer modulus (remainder): ",result)

result = abs(-7)
print("Absolute value: ", result)

result1 = round(24.738886, 2)
print(result1)

# String strip
text = "   Some spaces around    "
stripped_text =  text.strip()
print("Stripped text:",stripped_text)

# regex-search in in string
import re
text = "The regular quick"
pattern = r"quick"
search = re.search(pattern, text)
if search:
    print("search found:",search.group())
else:
    print("No search")    

# regex-replace in string
import re
text ="I like Python"
new_string = re.sub("Python", "Java", text)
print(new_string)

# replace in string
text = "I like C language"
result = text.replace("C", "Python")
print(result)
