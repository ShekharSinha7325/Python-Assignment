# Q12. Write a program that calculates the library charge based on the number of days a
# book has been borrowed.

number_of_Days = int(input(" Enter the number of days the book has been borrowed : "))
if number_of_Days <= 5:
    print(f" The library charge : ₹ {number_of_Days * 2 } ")
elif number_of_Days >= 6 and number_of_Days <= 10:
    print(f"The library charge : ₹ {number_of_Days * 3}")
elif number_of_Days >= 11 and number_of_Days <= 15:
    print(f"The library charge : ₹ {number_of_Days * 4}")
elif number_of_Days > 15 :
    print(f"The library charge : ₹ {number_of_Days * 5}")