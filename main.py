student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    grade = ""
    if student_scores[name] <= 70:
        grade = "Fail"
    elif student_scores[name] <=80:
        grade = "Acceptable"
    elif student_scores[name] <=90:
        grade = "Exceeds Expectations"
    elif student_scores[name] <=100:
        grade = "Outstanding"
    
    student_grades[name] = grade
    

# 🚨 Don't change the code below 👇
print(student_grades)





