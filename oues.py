num = int(input("enter your number"))
if  num % 2 == 0 :
    print("even number")
else :
    print("odd number")    
num  = int(input("enter your value"))
if num > 0 :
    print("positive number")
elif num < 0 :
    print("negative number")
else :
    print("zero")
num1 = int(input("enter your first  number"))
num2 = int(input("enter your second number"))
if num1 > num2 :
    print("largest number is : " , num1)
elif num2 > num1 :
    print("largest number is :" , num2 )
else :
    print("both nmumber are equal")
# two num m ager largest number ka queston h toh srif >
#thre num m ager largest number h toh srif >=
num1 = int(input("enter your fiest number"))
num2 = int(input("enter your sencond number"))
num3 = int(input("enter your thrid number"))
if num1 >= num2 and num1 >= num3 :
    print("largest number is :" , num1)
elif num2 >= num1 and num2 >= num3 :
    print("largest number is :" , num2)    
else :
    print("largest number :" , num3)