#num = 1
#while num <= 10 :
   # print(num)
    #num += 1
#num = 2
#while num <= 20 :
   # print(num )
    #num += 2
#num = 1
#while num <= 100 :
   # print(num , sum)
    #num += 1
num = 1
while num <= 10 :
    print("7 x" , num , "=" , 7* num)
    num += 1        
num = 1234
reverse = 0
while  num > 0 :
    digit = num % 10 
    reverse = reverse * 10 + digit
    num = num // 10
    print(" Reversed Number =" , reverse) 

#while num >= 1 :
   # print(num)
    #num -= 1
num = int(input("enter a number :" ))
i = 2
is_prime = True
while i <num :
    if num % i == 0 :
        is_prime = False
        break
    i += 1
if num > 1 and is_prime :
    print("prime number")
else :
    print ("not a prime number")        


num = int(input("enter an integer :"))
count = 0
while num != 0 :
    num = num // 10
    count += 1
print("number of digits =" , count)    


list = ["mango", "apple"] 
for i in list :
    print(i)

list = [1, 2, 3 , 4]  
for i in range (1 , 4) :
    print(i)
