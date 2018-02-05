

def main():
    
    days = dict(
                one = "Monday",
                two = "Tuesday",
                three = "Wednesday"
                
                )
    day1 = "one"
    day2 = "four"
    print(days[day1])
    print(days.get(day2, 'No Match'))




if __name__ == "__main__": main()

