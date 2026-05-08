# Q14. Calculate compound interest
# Input: principal = 10000, rate = 5, time = 2 
# Output: Compound Interest = ?

principal = 10000
rate = 5
time = 2

compound_interest = (principal*(1+ rate/100)**time)-principal
print(f"Compound Interest is :  {compound_interest}")