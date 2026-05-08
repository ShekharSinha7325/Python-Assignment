# Q7. you have to design a Program that checks whether a student is
# eligible for an interview based on their academic score attendance percentage
# and extracurricular participation

Academic_Score = float(input("Enter Your Academic Score : "))
Attendance_percentage = float(input("Enter Your Attendance Percentage : "))
Extracurricular_Participation = str(input("You participated in any extracurricular activities(Yes/No) : "))

#check the conditions for interview Eligibility
if(Academic_Score >= 60 and Attendance_percentage >= 75
   and Extracurricular_Participation.lower() == "yes"):   
    print("You are Eligible For Interview ")
else:
    print("Not Eligible For Interview")

# Hint :-
# input() always stores data as string by default
# User enters Yes/No, so we use string comparison ("yes")
# not int or boolean
# .lower() converts user input into lowercase
# so YES, Yes, yes all become "yes"
# This helps avoid case-sensitive problems