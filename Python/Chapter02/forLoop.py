
#syntax
# for loop
#     for each in collection:
#         print(each)

def main():    
        print("Hello")
        
        #value = [1, 2, 3, 4, 5, 6]
        #value = (1, 2, 3, 4, 5, 6)
#         value = "This is a string"
#      
#      
#         for i in value:
#             print(i, end=' ')
        
         
        value = "This is a string"
        # to track an index we can use a function called enumerate which is a collection of data, return us two values
     
        for index, charac in enumerate(value):
            print(index, charac)
            
            




if __name__ == "__main__": main()

