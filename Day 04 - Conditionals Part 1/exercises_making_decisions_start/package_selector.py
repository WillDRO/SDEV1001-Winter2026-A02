
print("Welcome to the Ultimate Gym")
print("Please select a membership package: ")
print(" - Package A: $40/month, 4 months (short-term package)")
print(" - Package B: $55/month, 8 months (standard package)")
print(" - Package C: $75/month, 12 months (regular package)")
print(" - Package D: $100/month, 12 month (premium package, includes 4 free personal training sessions)")



user_choice = input("Enter the package letter (A/B/C/D): ")



if user_choice == "A":
    print("You have selected Package A")
    print("Your monthly fee is $40")
    print("Your total fee is $160")

elif user_choice == "B":
    print("You have selected Package B")
    print("Your monthly fee is $55")
    print("Your total fee is $440")

elif user_choice == "C":
    print("You have selected Package C")
    print("Your monthly fee is $75")
    print("Your total fee is $900")

elif user_choice == "D":
    print("You have selected Package D")
    print("Your monthly fee is $100")
    print("Your total fee is $1200")
