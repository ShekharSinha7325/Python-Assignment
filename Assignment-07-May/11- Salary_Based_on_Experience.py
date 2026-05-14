# Q11.You are building a system for a Human Resources (HR) department that calculates anemployee's salary
# based on their years of experience. The system assigns salary tiers based on the number of years an employee 
# has been working. It also offers bonuses for employees who have more than 15 years of experience.


employee_experience = int(input("Enter Your Experience : "))
if employee_experience >= 10:
    salary = 80000
    bonus = 5000
    print("Senior employee")
    if employee_experience > 15:
        print("Experience exceeds 15 years. Bonus added.")
        print(f"Salary : {salary + bonus}")
    else:
        print(f"Salary : {salary}")
if employee_experience >= 5 and employee_experience <= 9:
    salary = 50000
    print("Mid-level employee")
    print(f"Salary : {salary}")
if employee_experience > 0 and employee_experience <= 5 :
    salary = 30000
    print("Junior employee")
    print(f"Salary : {salary}")