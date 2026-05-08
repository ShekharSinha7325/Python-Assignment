# Q4.Write a program to calculate the area of a circle

radius_of_Circle = float(input("Enter The radius of a Circle : "))
# The formula of the area of the circle : Area = π *radius^2.  π = 22/7, 3.14, define math.pi
Area_of_Circle = (22/7 *radius_of_Circle**2)

# .2f is used to display float value up to 2 decimal places
print(f"The Area of Circle is = {Area_of_Circle:.2f} m²")