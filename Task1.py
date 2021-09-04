#1 WAP for addition, subtraction, multiplication, and division:-

'''num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)'''

#2 WAP to calculate simple interest:-

'''principal = float(input('Enter the principle amount: '))
time = float(input('Enter the time: '))
rate = float(input('Enter the rate: '))
simple_interest = (principal*time*rate)/100
print("Simple interest is:", simple_interest)'''

#3 WAP for swapping using third variable:-
'''
x = 10
y = 50

temp = x
x = y
y = temp
 
print("Value of x:", x)
print("Value of y:", y)'''

#4 WAP for swapping without using third variable:-
'''
x = 5
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)'''

#5 WAP to calculate gross salary from basic salary(HRA=30%, TA=40%, DA=20%):-

'''basic=float(input("Enter Basic Salary :"))
hra=float(basic*0.30)
ta=float(basic*0.40)
da=float(basic*0.20)
gross_salary=float(basic+da+hra+ta)
print('Gross Salary:',gross_salary)'''

#6 WAP to find circumference of circle:-

'''print("Enter Radius of Circle: ")
r = float(input())
c = 2*3.14*r
print("Circumference of Circle is:-  ", c)'''

#7 WAP to find area of circle:-

'''print("Enter the value of Radius r:")
r = float(input())
Area = 3.14*r*r
print("Area of Circle is:- ", Area)'''

#8 WAP to enter height of user in feets and convert it into inches and centimeter
# 1 feet = 12 inch
# 1 inch = 2.54 cm

'''print("Input your height in feets: ")
h_ft = float(input())
h_inch = h_ft * 12
h_cm = round(h_inch * 2.54, 1)
print("Your height is : %f inches." % h_inch)
print("Your height is : %f cm." % h_cm)'''

#9 WAP to reverse three number (123 = 321)

'''n = 123
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print("Number in reverse: ", rev)'''

#10 WAP to take centigrade temperature and convert it into fahrenheit temperature (f= 1.8*c + 32)

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit is: ", fahrenheit)