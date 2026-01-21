#The year of the zodiac sign is based on a 12 year cycle.
year = int(input("Enter a year: "))

if year % 12 == 0:
    print("sheep")
elif year % 12 == 1:
    print("monkey")
elif year % 12 == 2:
    print("dog")
elif year % 12 == 3:
    print("pig")
elif year % 12 == 4:
    print("rat")
elif year % 12 == 5:
    print("ox")
elif year % 12 == 6:
    print("tiger")
elif year % 12 == 7:
    print("rabbit")
elif year % 12 == 8:
    print("dragon")
elif year % 12 == 9:
    print("snake")
elif year % 12 == 10:
    print("horse")
else:
    print("sheep")
