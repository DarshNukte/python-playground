height = int(input("What is your height?\n"))
toBePaid = 0

if height >= 120:
    age = int(input("What is your age?\n"))
    if age <= 12:
        print("Child tickets are $5.")
        toBePaid = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        toBePaid = 7
    else:
        print("Adult tickets are $12.")
        toBePaid = 12
    if input("Do you want a photo take? (Y/N)") == "Y":
        toBePaid += 3
    print(f"Your total bill would be ${toBePaid}.")
else:
    print("Sorry, you need to grow taller before you can ride.")
