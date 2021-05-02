def removeDuplicateAndSortWords(inputValue):
    newValueList=list(set(list(inputValue.split(' '))))
    newValueList.sort()
    print(newValueList)
    print(' '.join(map(str, newValueList)))
removeDuplicateAndSortWords(input())