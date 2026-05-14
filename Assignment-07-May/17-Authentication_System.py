# Q17. Write a program to authenticate a user by validating their username and password.

user_Name = input("Enter User Name : ").lower()
user_password = input("Enter your Password : ").lower()
 
username = "user1"
password = "pass@123"

if username == user_Name and user_password == password:
    print("Authentication successful.")
else:
    print("Authentication failed")

