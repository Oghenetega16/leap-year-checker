def leap_year(year):
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("The year", year, "is a leap year.")
            else:
                print("The year", year, "is not a leap year.")
        else:
            print("The year", year, "is a leap year.")
    else:
        print("The year", year, "is not a leap year.")

year = int(input("Enter a year: "))    
leap_year(year)