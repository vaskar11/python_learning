#23. Dictionary, List, & Set: Given a list of students and their grades, create a dictionary that groups  students by their grade, and return a set of all unique grades.

students_grades = [(12,"Bhaskar"),[32,"Hari"],[32,"Gopal"],[90,"Rita"],[29,"Gita"]]
grade_dict = {} 
unique_grades = set() 
for student, grade in students_grades: 
    if grade not in grade_dict: 
       grade_dict[grade] = []  
grade_dict[grade].append(student) 
unique_grades.add(grade) 
print(grade_dict) 
print(unique_grades) 