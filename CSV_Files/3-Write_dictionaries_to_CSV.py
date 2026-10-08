import csv 

students = [ {"name": "Asha", "age": 20}, 
            {"name": "Ravi", "age": 21} ]

with open("students.csv", "w", newline="", encoding="utf-8") as file: 
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader() 
    writer.writerows(students)
                                            