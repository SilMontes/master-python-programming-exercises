import math

valuesOf = input()
valuesofD=valuesOf.split(',')
newValues = list(map(lambda value:  round(math.sqrt(2 * 50 * int(round(float(value))) / 30)), valuesofD))
print(newValues)
