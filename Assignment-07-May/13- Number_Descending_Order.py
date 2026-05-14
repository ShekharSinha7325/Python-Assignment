# @13. Write a program to arrange three numbers in descending order.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter Third  number : "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 > num1 and num2 > num3:
    if num1 > num3 :
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 > num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)


# Another way to solve this using swaping in python 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# # Swap logic for descending order

# if a < b:
#     a, b = b, a

# if a < c:
#     a, c = c, a

# if b < c:
#     b, c = c, b

# print("Descending order:", a, b, c)