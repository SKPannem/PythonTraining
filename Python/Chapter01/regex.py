#regularExpression

import re

def main():
    print("Hello World")   

    file = open("google.txt")
    
    for i in file:
        patternMatch = re.search("(P|p)ython", i)
        if patternMatch:
            print(patternMatch.group())


if __name__ == "__main__": main()
