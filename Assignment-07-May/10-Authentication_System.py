# Q10. Write a program that authenticates a user by checking their username and
# password. The program should compare the entered credentials with predefined valid credentials.

user_Name = input("Enter your UserName : ")
user_Password = input("Enter your Password : ")
userName1 = "user1"
username1_password1 = "pass@123"

if user_Name == userName1 and user_Password == username1_password1:
    print("Authentication successful")
else:
    print("Authentication failed ")