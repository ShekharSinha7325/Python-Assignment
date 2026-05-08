# Q5.You have to calculate an employee's salary by computing the gross
# salary tax and net salary based on the given parameters.

Base_Salary =float(input("Enter Your Basic Salary : "))
Allowances = float(input("Enter Your  Allowances : "))
Tax_Rate = float(input("Enter Tax Rate : "))

# Calculate gross salary
Gross_Salary = Base_Salary + Allowances

#Calculate Tax 
Tax = (Tax_Rate / 100) *Gross_Salary
Net_Salary = Gross_Salary - Tax
# .2f is used to display float value up to 2 decimal places
print(f"Your Gross Salary is : {Gross_Salary:.2f}")
print(f"Tax Amount is : {Tax:.2f}")
print(f"Your Net Salary is : {Net_Salary:.2f}")


