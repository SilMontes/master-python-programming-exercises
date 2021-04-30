#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
    for number in range(1,366):
        if k % 7 == 1 or k == 1:
            return 4
        elif k % 7 == 2 or k == 2:
            return 5
        elif k % 7 == 3 or k == 3:
            return 6
        elif k % 7 == 4 or k == 4:
            return 0
        elif k % 7 == 5 or k == 5:
            return 1
        elif k % 7 == 6 or k == 6:
            return 2
        elif k % 7 == 0 or k == 7:
            return 3
         
    #return None

#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(1))
print(56%7)
print(21%7)