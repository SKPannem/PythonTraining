
#Assign
def main():
    highScore = 1
    print(highScore)
    
    
    highScore = 1
    print(type(highScore),highScore)
    
    highScore = "1" #Anything in a double quotes is a string whether it is an integer or high level
    print(type(highScore),highScore)
    
    highScore = 1.5
    print(type(highScore),highScore)
    
    a, b = 1, 2
    a,b = b, a
    print(a, b)
    
if __name__ == "__main__": main()

