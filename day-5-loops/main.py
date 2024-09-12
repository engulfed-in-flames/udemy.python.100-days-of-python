import random

# fmt: off
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "*"]

print("Welcome to the PyPassword Generator!")
len_letters = int(input("How many alphabets would you like in your password?\n"))
len_symbols = int(input("How many symbols would you like?\n"))
len_numbers = int(input("How many numbers would you like?\n"))

# Easy Version
random_alphabets = "".join(random.choices(alphabets, k=len_letters))
random_symbols = "".join(random.choices(symbols, k=len_symbols))
random_numbers = "".join(random.choices(numbers, k=len_numbers))
password_easy = random_alphabets + random_symbols + random_numbers
print(f"The generated password is: {password_easy}")

# Hard Version
password_hard = list(password_easy)
random.shuffle(password_hard)
password_hard = "".join(password_hard)

print(f"The generated password is: {password_hard}")
