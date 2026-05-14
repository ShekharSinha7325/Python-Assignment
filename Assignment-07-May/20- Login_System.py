# Q20. Create the Menu:
# ○ Display a menu with three choices for the user:
# ■ Login with Phone
# ■ Login with Email
# ■ Exit the system

phone_number = "1234567890"
otp = "1234"

email = "user@example.com"
password = "password123"

#Menu 
print("1. login with phone")
print("2. login with email")
print("3. Exit")

choice = int(input("Enter your Choice : "))

#option 1
if choice == 1:
    user_phone = input("Enter Your phone number : ")
    user_otp = input("Enter Your otp : ")

    if user_phone == phone_number and user_otp == otp:
        print("Login successful")
    
    else:
        print("Invail phone number and otp")

#option 2

elif choice == 2:
    user_email = input("Enter your email :")
    user_password = input("Enter your password : ")

    if user_email == email and user_password == password:
        print("Login successful")
    else:
        print("Invalid email and password ")

#option 3
elif choice == 3:
    print("Exiting the program. Have a nice day!")

else:
    print("Invaild  choice : please slect again.")