# Q3.Write a program that prompts the user for their age and tells them how
# many years until they reach retirement age (65).

User_Age = int(input("Enter Your Age  : "))
retirement_Age = 65
# Calculate remaining years
year_left = retirement_Age - User_Age
if User_Age < retirement_Age:
    print(f"You have {year_left} years left untill retirement ")
else:
    print("You have already reached retirement age")