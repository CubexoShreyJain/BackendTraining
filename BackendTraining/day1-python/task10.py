x = input("Enter something: ")

if x.isdigit():
    print("You entered a number.")
elif x.replace(".", "", 1).isdigit():
    print("You entered a floating-point number.")
elif x.isalpha():
    print("You entered a string of letters.")
else:
    print("You entered something else.")