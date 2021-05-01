def itemsList():
    values=input("Input some comma seprated numbers : ")
    newList=values.split(',')
    newTuple=tuple(newList)
    print(newTuple)
itemsList()