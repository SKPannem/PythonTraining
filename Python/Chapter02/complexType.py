from test.test_pprint import dict2, dict3

def main():
    
    #Tuple:
    
    tup = (3, 4, 5, 6)
    #fixed can't be changed or insert or delete any value from them
    #tuples can be used for Account num, SSN, etc
    print(tup)
    
    #List:
    
    list = [3, 4, 5, 6]
    #square brackets
    list.append(7)
    print(list)
    
    list.insert(1, 9) #index starts with 0 so when 9 is given in 1's place. in output it prints 9 in 1's place.
    print(list)
    
    #Dictionary:
    dict1 = {'one':1, 2: 'two'} 
    #one is key ,1 is value similarly 2 is value and two is key
    # key, value pairs          
    print(dict1)                  
    
    dict2 = dict([('one',1),('two',2)])
    print(dict2)
    
    dict3 = dict(one = 1, two = 2)
    print(dict3)
    
    
if __name__ == "__main__": main()
