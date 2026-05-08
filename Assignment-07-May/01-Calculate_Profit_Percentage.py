# Q1.Write a program that takes input for the cost price and selling price of an item.

cost_price = float(input("Enter Cost Price : "))
selling_price = float(input("Enter selling Price : "))
profit = selling_price - cost_price
profit_percentage = (profit / cost_price) *100
loss = cost_price - selling_price
loss_percentage =  (loss/cost_price)*100
if cost_price < selling_price:
    print(f"Profit  = {profit}")
    if profit:
        # round(value, 2) is used to show only 2 digits after decimal
        print(f"Profit Percentage is  = {round(profit_percentage,2)} %")
if cost_price > selling_price:
    print(f"Loss  = {loss}")
    if loss:
        # .2f is used to display float value up to 2 decimal places
        print(f"Loss percentage = {loss_percentage:.2f} %")