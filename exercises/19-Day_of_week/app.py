#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
    for number in range(1,365):
        if number / 7 == 1 or number == 1:
            k = "Thursday"
            print(str(number),k)
        elif number / 7 == 2 or number == 2:
            k = "Friday"
            print(str(number),k)
        elif number / 7 == 3 or number == 3:
            k = "Saturday"
            print(str(number),k)
        elif number / 7 == 4 or number == 4:
            k = "Sunday"
            print(str(number),k)
        elif number / 7 == 5 or number == 5:
            k = "Monday"
            print(str(number),k)
        elif number / 7 == 6 or number == 6:
            k = "Tuesday"
            print(str(number),k)
        elif number / 7 == 0 or number == 7:
            k="Wednesday"
         
        return k
    #return None

#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(2))