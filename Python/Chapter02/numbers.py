

def main():
    
    balance0 = (88/9)
    balance1 = (88//9)
    balance2 = int(5.65)   #converting 5.65 to int
    balance3 = float(6)    #converting 6 to float
    balance4 = round(88/9) #round the value  
    balance5 = round(88/9, 4) #round the value till digit 4
    balance6 = 88 % 9       # % gives the remainder
    
    
    balance7 = int(9.5)
    #int and float functions are constructors in this case
    #calling an constructor int and passing the value 9.5 and try to create a new object
    
    print(type(balance0),balance0)
    print(type(balance1),balance1)
    print(type(balance2),balance2)
    print(type(balance3),balance3)
    print(type(balance4),balance4)
    print(type(balance5),balance5)
    print(type(balance6),balance6)
    print(type(balance7),balance7)
    
if __name__ == "__main__": main()
