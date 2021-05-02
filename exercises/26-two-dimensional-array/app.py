import random
def twoDimensionalArray(digitRow,digitColumn):
    newList=[]
    for item in range(digitRow):
        newListItem=[]
        for number in range(digitColumn):
            newListItem.append(item*number)
        newList.append(newListItem)
    return(newList)
print(twoDimensionalArray(3,5))


