passed_grades = 0
failed_grades = 0
total_sum = 0
passed_sum = 0
failed_sum = 0
counter = 1
total_grades = 0
grade = 0

total_grades = int(input("Enter the number of grades: "))

while counter <= total_grades:
    grade = float(input("Enter the grade obtained: "))
    print("Grade", counter, ":", grade)
    total_sum += grade
    counter += 1
    
    if grade >= 70:
        passed_grades += 1
        passed_sum += grade
    else:
        failed_grades += 1
        failed_sum += grade

print("Number of passed grades:", passed_grades)
print("Number of failed grades:", failed_grades)
print("Average of all grades:", total_sum / total_grades)

if passed_grades > 0:
    print("Average of passed grades:", passed_sum / passed_grades)
else:
    print("There are no passed grades to calculate the average.")

if failed_grades > 0:
    print("Average of failed grades:", failed_sum / failed_grades)
else:
    print("There are no failed grades to calculate the average.")