# write a script accept a number and check the given
# number is an Even  or Odd number

n=int(input("Enter a number : "))

if   n%2==0 :
    print(n,"is an Even number")
    print("Hello GM to all")
    print("Have a Greate day")
else :
    print(n,"is an Odd number")
    
##########################################################################

# WAS accept a number and check the given number is
# 3 digit or not

n=int(input("Enter a number : "))

if   abs(n)>=100  and   abs(n)<=999 :
    print(n,"is a 3 digit number")
else :
    print(n,"is not a 3 digit number")
    
##########################################################################

# Login program

uname=input("Enter a username : ")
pwd=input("Enter a password :")

if  uname=="tecno"   and  pwd=="python1" :
    print("Welcome to Python class")
else :
    print("Invalid username or password")

##########################################################################

# Guess number

n=int(input("Enter a guess [1-10 ] : "))

if  n==3 :
    print("Wow.Your guess is correct")
else :
    print("Sorry.Your guess is worng")
    
##########################################################################

# Guess number

import random

n=int(input("Enter a guess [1-10 ] : "))

x=random.randint(1,10)

if  n==x :
    print("Wow.Your guess is correct")
else :
    print("Sorry.Your guess is worng.I was thinking ",x)

##########################################################################

# Write a script accept empno,ename,job and salary and
#calculate bonus based on the following condtions

#job       bonus
#manager    20% on ann_sal
#analyst    18% on ann_sal
#programmer 15% on ann_sal
#salesman   12% on ann_sal
#others     10% on ann_sal

empno=int(input("Enter a  empno : "))
ename=input("Enter a ename : ")
job=input("Enter a job : ")
sal=int(input("Enter a salary : "))

ann_sal=sal*12

if job=="manager":  bonus=ann_sal*20/100
elif job=="analyst" : bonus=ann_sal*18/100
elif job=="programmer" :bonus=ann_sal*15/100
elif job=="salesman" : bonus=ann_sal*12/100
else : bonus=ann_sal*10/100

print("#"   *  40)
print( "###   Employee Bonus Report  ####")
print( "-" * 40)
print( "###   Employee Number  : ",empno, " ###")
print( "###   Employee Name    : ",ename, " ###")
print( "###   Employee Job     : ",job, " ###")
print ("###   Employee Salary  : ",sal, " ###")
print( "###   Employee AnnSal  : ",ann_sal, " ###")
print("###   Employee Bonus   : ",bonus, " ###")
print ( "-" * 40)
print( "#"   *  40)

##########################################################################

# write a script accept 2 number's and find greast number

a=int(input("Enter a number 1 : "))
b=int(input("Enter a number 2 : "))
if a!=b :
    if a>b :         
        print(a," is big")
    else :
        print(b," is big")
else :
    print("2 numbers are equal")

##########################################################################