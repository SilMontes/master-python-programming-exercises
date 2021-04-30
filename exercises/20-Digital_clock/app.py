#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
    hour=n//60
    minutes=n%60
    return (hour,minutes)

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))
print(150//60)