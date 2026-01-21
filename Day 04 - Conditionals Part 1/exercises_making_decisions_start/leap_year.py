


#Testing if user input is a leap year.
year = int(input("Enter a year: "))
#Leap years are divisible by 4 and should not divisible by 100 at the same time, 
# unless they are also divisible by 400.
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year? true")

else:
    print(f"{year} is a leap year? false")
    
