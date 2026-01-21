

user_choice = int(input("Enter a month number (1-12): "))

# Define month numbers
January, February, March, April, May, June, July, August, September, October, November, December = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

if user_choice == January:
    print("January")
elif user_choice == February:
    print("February")
elif user_choice == March:
    print("March")
elif user_choice == April:
    print("April")
elif user_choice == May:
    print("May")
elif user_choice == June:
    print("June")
elif user_choice == July:
    print("July")
elif user_choice == August:
    print("August")
elif user_choice == September:
    print("September")
elif user_choice == October:
    print("October")
elif user_choice == November:
    print("November")
else:  # December
    print("December")