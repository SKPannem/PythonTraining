

name="Hari"
age=18
print("Hello",name,",nice to meet you! and you are ",age,"years old")
#print("Hello"+name+",nice to meet you! and you are "+age+"years old")

##########################################################################

name=input("what is your name?")
age=input("What is your age?")
print("Hello",name,"nice to meet you and your are",age,"years old")

##########################################################################
# accept 2 numbers and find sum

a=input("Enter a number 1 : ")
b=input("Enter a number 2 : ")
c=int(a)+int(b)
print("Sum=",c)
print(type(a),type(b))

##########################################################################

# accept 2 numbers and find sum

a=int(input("Enter a number 1 : "))
b=int(input("Enter a number 2 : "))
c=a+b
print("Sum=",c)
print(type(a),type(b))

##########################################################################

# WAP accept Employee number,name and salary and calculate bonus
# based on the following condition (10% on ann_sal)

empno=int(input("Enter a employee number : "))  
ename=input("Enter a employee name : ")
esal=int(input("Enter a employee salary : "))

ann_sal=esal*12
bonus=ann_sal*10/100

print("\t\t  Employee Bonus Report ")
print("-" * 50)
print("\t Employee Number  : ",empno)
print("\t Employee Name    : ",ename)
print("\t Employee Salary  : ",esal)
print("\n\t Annual Salary  : ",ann_sal)
print("\t Employee Bonus   : ",bonus)
print("-" * 50)

##########################################################################

# WAP accept student name and 3 subject marks and
# calculate total marks and avg marks and prepare report.

sname=input("Enter astudent name : ")
marks1=int(input("Enter marks 1  : "))
marks2=int(input("Enter marks 2  : "))
marks3=int(input("Enter marks 3  : "))

total_marks=marks1+marks2+marks3
avg_marks=total_marks/3

print("\t\t  Student Progress Report ")
print("#" * 50)
print("\t Student name  :  ",sname)
print("\t Marks1        :  ",marks1)
print("\t Marks2        :  ",marks2)
print("\t Marks3        :  ",marks3)
print("\n\t Total Marks   :  ",total_marks)
print("\t Avg Marks     :  ",avg_marks)
print("#" * 50)

########################################################################## 