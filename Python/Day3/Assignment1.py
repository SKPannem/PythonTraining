
#Assignments
#-----------------------------------------------------------------
#1)WAP accept product no,pname,price,qty and 
#caluclate total,disc(10% on total),
#and net amount and prepare bill


productNo = input(("Enter the Product Number : " ))
pname = input(("Enter the Product Name : " ))
price = input(("Enter the Price : "))
qty = input(("Enter the Quantity : " ))
 
netAmount = int(price)*int(qty)
calculateTotal = netAmount*10/100
 
print("*" * 50)
print("\t '''Product Bills Report'''")
print("-" * 50)
print("\t Product Number:", productNo)
print("\t Product Name:", pname)
print("\t Price:", price)
print("\t Quantity:", qty)
print("-" * 50)
print("\n \t Net Amount:", netAmount)
print("\t Calculate Total:", calculateTotal)
print("*" * 50)

#-----------------------------------------------------------------

#2) WAP accept studentname and  3 subject marks and calculate
#total and avg marks and prepare report

studentName = input("Entre the Student Name : ")
submarks1 = int(input("Enter Subject Marks 1 : "))
submarks2 = int(input("Enter Subject Marks 2 : "))
submarks3 = int(input("Enter Subject Marks 3 : "))
 
calculate_total = submarks1+submarks2+submarks3
avg_marks = calculate_total/3
 
print("#" * 50)
print("\t Students Progress Report")
print("-" * 50)
print("\t Student Name :",studentName)
print("\t Subject Marks 1 :",submarks1)
print("\t Subject Marks 2 :",submarks2)
print("\t Subject Marks 3 :",submarks3)
print("\n \t Total Calculation :",calculate_total)
print("\t Average Marks :",avg_marks)
print("#" * 50)
 

#-----------------------------------------------------------------

#3) WAP accept empno,ename,sal and
#calculate ta,da,hra,total_allowences and gross salary
#and prepare employee pay slip

# ta  =>  10% 0n sal
# da  => 15% on sal
# hra => 20% on sal
# total_allow => ta+da+hra
# gross_sal => sal+total_allow

empNo = input("Enter the Employee NUmber : ")
eName = input("Enter the Employee Name : ")
sal =  int(input("Enter the Salary : "))

ta = sal*10/100
da = sal*15/100
hra = sal*20/100
total_allow = ta+da+hra
gross_sal = sal+total_allow

print("#" * 50)
print("\t Employee Salary Report")
print("-" * 50)
print("\t Employee Number : ",empNo)
print("\t Employee Name : ",eName)
print("\t Employee Salary : ",sal) 
print("\n \t ta : ",ta)
print("\t da : ",da)
print("\t hra : ",hra)
print("-" * 50)
print("\t Total Allows : ",total_allow)
print("\t Gross Salary : ",gross_sal)
print("#" * 50)
          





#-----------------------------------------------------------------