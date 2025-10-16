import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

print("Welcome to PyPassword Generator.")
amt_letters = int(input("How many letters do you want?\n"))
amt_symbols = int(input("How many symbols do you want?\n"))
amt_numbers = int(input("How many numbers do you want?\n"))

password = ""
fpassword = ""

for char in range(1, amt_letters + 1):
    password += random.choice(letters)
for num in range(1, amt_numbers + 1):
    password += random.choice(numbers)
for sym in range(1, amt_symbols + 1):
    password += random.choice(symbols)

# print(password)
passlist = []
for item in range(0, len(password)):
    passlist.append(password[item])
for itema in range(0, len(password)):
    fpassword += random.choice(passlist)

print(f"Your password is {fpassword}")
