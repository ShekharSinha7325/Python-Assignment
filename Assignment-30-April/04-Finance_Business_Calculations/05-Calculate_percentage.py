# Q16. Calculate percentage increase or decrease 
# Input: initial_value = 200, final_value = 250 
# Output: Percentage Change = ? 

initial_value = 200
final_value = 250
percentage_change = ((final_value - initial_value)/initial_value)*100

if percentage_change > 0:
    print(f"percentage increase = {percentage_change} %")
elif percentage_change < 0:
    print(f"percentage decrease = {percentage_change}%")
else:
    print("No change")


    