"""

"""

def leapYear(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return "a leap year"
            else:
                return "an ordinary year"
        else:
            return "a leap year"
    else:
        return "an ordinary year"

year = int(input("Enter a year: "))
print(f"{year} is {leapYear(year)}.")
