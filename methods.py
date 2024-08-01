def leap_year(year):
    if((year%400)==0 or(year%100==0 and year%4==0)):
        print("Its a leap year")
    else:
        print("Not a leap year")