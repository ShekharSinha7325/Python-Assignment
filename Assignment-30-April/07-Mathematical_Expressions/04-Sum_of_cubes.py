# Q29.Sum of cubes: a³ + b³ 
# Input: a = 1, b = 2 
# Output: ? 

a = 1
b = 2

result = (a + b) *(a**2 + b**2 - a*b) # formulla (a^{3}+b^{3}=(a+b)(a^{2}-ab+b^{2})

print(f"Sum of cubes = {result}")
