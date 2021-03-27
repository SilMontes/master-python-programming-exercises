#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    aggregate1=(hr1*3600)+(min1*60)+sec1
    aggregate2=(hr2*3600)+(min2*60)+sec2
    return aggregate2-aggregate1


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))