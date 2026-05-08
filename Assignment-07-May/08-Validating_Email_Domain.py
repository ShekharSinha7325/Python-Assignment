# Q8. You will implement a  program to validate the domain of a
# user's email address. The program will check if the email contains a specific
# domain (e.g. "gmail.com").

# Take input From The User

email_address = str(input("Enter Your Email : "))

if "@" in email_address and "gmail.com" in email_address:
    print(f"Validate email : {email_address}")
else:
    print(f"Invalid email : {email_address} ")
