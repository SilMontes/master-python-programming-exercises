#Complete the function to return the amount of days it will take to cover a route.
#HINT: You may need to import the math module for this exercise.
import math
def car_route(n,m):
    amount_days=m/n
    return math.ceil(amount_days)


#Invoke the function with two intergers.
print(car_route(700,750))