# Q.14. Write a program to calculate the tax on a car purchase based on the car brand and its price.

Car_brand = input("Enter the Car Brand : ").lower()
car_price = float(input("Enter the car Price(in lakh) : "))

# Mahindra
if Car_brand == "mahindra" and car_price >= 700000 and car_price <= 1000000:
    tax_rate = 5  # 5/100 = 0.05
    Tax = car_price * 0.05
    print(f"Tax on the purchase : ₹ {Tax}")
    
# Audi
elif Car_brand == "audi" and car_price >= 1000000 and car_price <= 1500000:
    tax_rate = 10  # 5/100 = 0.01
    Tax = car_price * 0.01
    print(f"Tax on the purchase : ₹ {Tax}")

# Jaguar
elif Car_brand == "jaguar" and car_price >= 1500000 and car_price <= 2000000:
    tax_rate = 25  # 5/100 = 0.25
    Tax = car_price * 0.25
    print(f"Tax on the purchase : ₹ {Tax}")

# Mercedes
elif Car_brand == "mercedes" and car_price >= 2000000 and car_price <= 2500000:
    tax_rate = 30  # 5/100 = 0.3
    Tax = car_price * 0.3
    print(f"Tax on the purchase : ₹ {Tax}")
else:
    print("Invalid Brand & price range")