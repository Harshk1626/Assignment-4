#Question 1

grade= float(input(" Enter your marks "))

if grade<25:
    print("Your final grade is F")
elif grade>=25 and grade<45:
    print("Your final grade is E")
elif grade>=45 and grade<50:
    print("Your final grade is D")
elif grade>=50 and grade<60:
    print("Your final grade is C")
elif grade>=60 and grade<80:
    print("Your final grade is B")
elif grade>=80 and grade<=100:
    print("Your final grade is A")
else:
    print("Error: You have entered incorrect data")
    
    
#Question 2

yr= int(input(" Enter the year: "))

if yr % 100 == 0:
    if yr % 400 == 0:
        print("The year ",yr," is a leap year!")
    else:
        print("The year ",yr," is not a leap year :(")
elif year % 4 == 0:
    print("The year ",yr," is a leap year!")
else:
    print("The year ",yr," is not a leap year :(")


#Question 3

from random import randint

for loop_variable in range(10):
    x = randint(0,10)
    y = randint(0,10)
    if int(input('Question: ' + str(x) + ' x ' + str(y) + ' = ')) == x * y: print('Right!')
    else: print('Wrong. The answer is ', x * y)


#Question 4

n=1
while n<200:
    if n%5 == 2 and n%6 == 3 and n%7 == 2:
        print("The number is: " + str(n))
    n = n + 1
