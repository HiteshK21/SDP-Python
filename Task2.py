#1 WAP for sum of natural numbers from 1 to 10:-

num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  

#2 WAP to calculate factorial of any number(5! = 120)

'''def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
num = 5;
print("Factorial of",num,"is",
factorial(num))'''

#3 WAP to calculate fibonacci series :-

'''a=int(input("Enter the terms"))
f=0                                         
s=1                                      
if a<=0:
    print("The requested series is",f)

else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next'''

#4 WAP to print LCM, HCF, GCD:-
'''
# For LCM:-
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 20
num2 = 64

print("The L.C.M. is", compute_lcm(num1, num2))

# For HCF/GCD:-
def calculate_hcf(x, y):   
    if x > y:  
        smaller = y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return hcf    
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
print("The H.C.F. of", num1,"and", num2,"is", calculate_hcf(num1, num2))  '''

#5 WAP to print leap year:-

'''def checkYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False
 
year = int(input("Enter the Year: "))
if(checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")'''

#6 WAP to find Armstrong number:-

'''num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")'''

#7 WAP to find Palindrome number:-

'''n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")'''

