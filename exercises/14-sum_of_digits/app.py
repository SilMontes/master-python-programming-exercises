#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
    num1=num//100 #obtener centenas
    num2=(num%100)//10 #obtener decenas
    num3=(num%10) #obtener unidades
    return num1+num2+num3


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(143))