for   i   in (1,2,3,4,5) :
    print(i)
##########################################################################

for   i   in list(range(1,11)) :
    print(i)
##########################################################################

for   i   in ('Unix','Perl','Python','Oracle') :
    print(i)    

##########################################################################
for   i   in "Python" :
    print(i)
    #print(i,end=" ")
    
    
##########################################################################

for   i   in "4598" :
    print(i)

'''

for   i  in   4598 :  #  Invalid
    print(i)
'''
##########################################################################

#1) Accept a string and find length of the string without
# Using len() function

x=input("Enter a string : ")  # Tecno

cnt=0
for   i   in  x :
    cnt=cnt+1

print("Lenght =",cnt)
##########################################################################

#2) Write a python script accept a string and count no.of vowels in a given
#string

x=input("Enter a string : ")  # Tecnosoft

cnt=0

for   i  in   x :
    if   i   in  "aeiouAEIOU" :
        cnt=cnt+1

print("No.of vowels in a",x,"string is : ",cnt)

##########################################################################

#3) Write a python script accept a string and count each vowel separately

x=input("Enter a string : ")  # Tecnosoft

a=e=i=o=u=0

for   k  in   x :
    if  k  in  "Aa" : a+=1  # a=a+1
    elif k in  "Ee" : e+=1
    elif k in  "Ii" : i+=1
    elif k in  "Oo" : o+=1
    elif k in  "Uu" : u+=1

print("Total no.of a's :",a)
print("Total no.of e's :",e)
print("Total no.of i's :",i)
print("Total no.of o's :",o)
print("Total no.of u's :",u)

##########################################################################

# 6) Write a python script accept a string and a character and remove
#the given character from string


x=input("Enter a string : ")  # Tecnosoft
ch=input("Enter a character to remove : ") # o
temp=""
if ch in x :  
    for   i  in  x :
        if i!=ch :
            temp=temp+i
    print("After removing ",ch,"character from",x,"string is :",temp)
else :
    print("Failed to delete,because",ch,"character not found in ",x,"string")

##########################################################################

#print Numbers from 1 to 10

i=1
while i<=10 :
    if i==5 :
        break
    print(i)
    i=i+1

##########################################################################

i=1
while i<=10 :
    if i==5 :
         break
    print(i)  #  1 2 3 4
    i=i+1

##########################################################################

i=1
while i<=10 :
    if i==5 :
        i=i+1
        continue
    print(i)  #  1 2 3 4 6 7 8 9 10
    i=i+1

##########################################################################







    





