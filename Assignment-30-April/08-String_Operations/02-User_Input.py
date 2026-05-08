# Q33.Create a Python program that asks the user for the following: 
# ● Full Name 
# ● Profession 
# ● Favorite Quote 
# ● Years of Experience 

# Output format: 
# Name        : <Full Name> 
# Profession  : <Profession>
# Experience  : <Years of Experience> years 
# Quote       : "<Favorite Quote>" 

full_Name = input("Enter Your full Name : ")
Profession = input("Enter Your Profession : ")
favorite_Quote = input("Enter Your favorite Quote : ")
Year_Of_Experience = input("Enter Your Year of Exprience : ")

print("\nFull Name :", full_Name)
print("Profession  :", Profession)
print("Experience  :", Year_Of_Experience, "years")
print('Quote       : "' + favorite_Quote + '"')