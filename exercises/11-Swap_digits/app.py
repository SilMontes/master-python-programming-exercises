#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
    left_digit=num%10
    right_digit=num//10
    return str(left_digit)+str(right_digit)
   
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(59))

