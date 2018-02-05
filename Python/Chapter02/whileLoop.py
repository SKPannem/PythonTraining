

def main():
    
    print("Hello")
    
    #Fibonacci Series Example problem
    #a series of numbers in which each number ( Fibonacci number ) is 
    #the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
    
    first = 0
    second = 1
    
    
    
    while first < 10:
        print(first, end=' ') #point of print, it shows end=\n which displays everything in different line.
        first, second = second, first + second
        
    


if __name__ == "__main__": main()