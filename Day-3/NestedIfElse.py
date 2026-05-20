height = int(input("What is your height?\n"))

if height >= 120:
    age = int(input("What is your age?\n"))
    if age <= 12:
        print("You can ride. You need to pay $5.")
    elif age <= 18:
        print("You can ride. You need to pay $7.")
    else:
        print("You can ride. You need to pay $12.")
else:
    print("Sorry, you need to grow taller before you can ride.")
