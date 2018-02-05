
'''
this is 
a multi line
comment
'''
from builtins import str

def main():

    str1 = 'This is \n one string'  #\n starts from next line
    str2 = r"This is two strings"  
    # r is the raw string method it can be used mostly in regex
    # When r is used it is raw string if not it is a double quotes string
    str3 = '''\
    This is third 
    string ending with 
    
    triple quotes''' #this counts the spaces and displays as it is and \ covers the blank space and continues to the current line
    str4 = """This is Fourth string"""
    
    balance = 90
    number = 80
    str = r"This is {} two {} strings".format(balance,number)
    # Here {} is replaced with 90 and followed by 80 and can add n- number of values
    
    
    
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    print(str)
    
if __name__ == "__main__": main()

