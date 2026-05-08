#Q12. Calculate profit or loss percentage 
# Input: cost_price = 500, selling_price = 600 
# Output: Profit or Loss = ?

cost_price = 500
selling_price = 600
profit = selling_price - cost_price
profit_percentage = (profit/cost_price)*100
loss = cost_price - selling_price
loss_percentage = (loss/cost_price)*100
if selling_price > cost_price :
    print(f"Profit = {profit}")
    print(f"Profit percentage = {profit_percentage}")
elif cost_price > selling_price:
    print(f" Loss =  {loss}")
    print(f"loss Percentage = {loss_percentage}")
else:
    print("Invaild Entry")