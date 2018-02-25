

def main():
    print("Hello World")
    
    lower = "i am a string"
    upper = "I AM A STRING"
    cash = 20
    
    
    print(lower.upper())
    print(upper.lower())
    print(upper.capitalize())
    newstring = upper.swapcase()
    print("old is", id(upper),  "and new is", id(newstring))
    print("i am a string too".upper())
    print("I got a {} $ cash".format(cash))
    
    print(lower.find('g'))
    print(lower.replace('am', 'will be'))
    
    userInput1 = "  I an a input  "
    userInput2 = "  I am input 2"


if __name__ == "__main__": main()