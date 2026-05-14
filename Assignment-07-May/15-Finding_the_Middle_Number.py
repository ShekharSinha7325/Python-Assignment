# Q15. Write a program to determine the middle number among three inputs.

num1 = int(input("Enter first Number  : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number  : "))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    middle_number = num1
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    middle_number = num2
else:
    middle_number = num3
print(f"Middle Number is : {middle_number}") 
