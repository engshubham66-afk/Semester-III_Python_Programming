import csv

rows = [ ["name", "age", "city"], 
        ["Asha", 20, "Delhi"], 
        ["Ravi", 21, "Mumbai"] ] 

with open("students.csv", "w", newline="", encoding="utf-8") as file:
     writer = csv.writer(file) 
     writer.writerows(rows) 
     