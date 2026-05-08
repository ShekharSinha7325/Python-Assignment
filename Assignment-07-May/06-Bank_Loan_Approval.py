# Q6. You have to create a Program that checks whether an user is
# eligible for a bank loan based on various criteria.

Applicant_Age = int(input("Enter Your Age : "))
Applicant_monthly_income = float(input("Enter Your monthly Income : "))
Applicant_Credit_Score = int(input("Enter Your Credit Score : "))
Applicant_outstanding_dept = float(input("Enter Your outstanding dept : "))

# Check All Condition for Loan Approval or Rejected
if(Applicant_Age >= 18 and Applicant_Age <= 60
   and Applicant_monthly_income >= 25000 and
   Applicant_Credit_Score >= 700 and
   Applicant_outstanding_dept > 10000):
    print("Loan Approved")
else:
    print("Loan Rejected")