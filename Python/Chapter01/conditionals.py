
#Conditionals
def main():
    scoreKevin = 100
    defaultHighScore = 100
    
    if scoreKevin > defaultHighScore:    
        print("Kevin you did that, congrats")
    
    elif scoreKevin < defaultHighScore:
        print("Try harder Kavin")
    
    else:
        print("Score equals to the default score")
        
    #OR can you this 
    
    msg = "you did it" if scoreKevin > defaultHighScore else "you didn't made it"
    print(msg)

    
if __name__ == "__main__": main()