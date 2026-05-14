# Q18. Write a program to calculate the percentage of classes attended by a student and 
# determine their eligibility to sit in the exam.

total_classes = int(input("Enter total number of classes held :"))
attented_classes = int(input("Enter total number of classes held :"))

attendance_percentage = (attented_classes/total_classes)*100
print(f"Your Attendance Percentage is:{attendance_percentage}%")

if attendance_percentage >= 75:
    print(f"""Eligible to sit in the exam : 
          your attedence percentage :{attendance_percentage} %""")

else:
    print("Not eligible to sit in the exam :")

