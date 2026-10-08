import csv

students = [ {"name": "Asha", "age": 20}, 
            {"name": "Ravi", "age": 21} ]

with open("students.csv", "r", newline="", encoding="utf-8") as file: 
    reader = csv.DictReader(file) 
    for row in reader: 
        print(row["name"], row["age"])