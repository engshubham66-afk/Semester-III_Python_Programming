# empty list
list1 = []
print(list1)

# list
list2 = [10, 'ankit',True, 10.6, 'ankush', 10]
print(list2[1])

# count method
print(list2.count(10))

# index
print(list2.index(10, 1))

# insert method 
list2.insert(2, "learn coding") 
print(list2)

# pop method
list2.pop(2)
print(list2)

# extend
list3 = ['shubham', 'sandeep']
list2.extend(list3)
print(list2)

# copy method
list3 = list2.copy()
print(list3)

# sort method
list4 = [10, 9, 17, 8,2, 16]
list4.sort() # acending order
print(list4)
list4.sort(reverse = True)
print(list4)

list5 = [1, 10, 4, 20]
list5.reverse()
print(list5)

# nested list
list6 = [10, 9, 17, ['uday', ['ritesh']] ]
print(list6)

# find words which starts from same letter
list7 = ['shubham', 'rohit', 'dev', 'deepak']
a = [word for word in list7 if word.startswith("d")]
print(a)