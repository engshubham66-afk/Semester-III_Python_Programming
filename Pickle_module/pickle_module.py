import pickle

student = {
    "name": "Asha",
    "marks": [80, 90, 85]
}

with open("student.pk1", "wb") as file:
    pickle.dump(student, file)

# read the obeject back

with open("student.pk1", "rb")  as file:
    student_data = pickle.load(file)

print(student_data)    