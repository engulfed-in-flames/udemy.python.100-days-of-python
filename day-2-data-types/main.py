# Tip Calculator
print("Welcome to the tip calculator!")

total_bill = input("What was the total bill?: $")
tip= input("How much tip would you like to give? 10, 12, or 15?: ")
number_of_people = input("How many people to split the bill?: ")

[total_bill, tip, number_of_people] = list(map(lambda el: float((el.strip())) ,[total_bill, tip, number_of_people]))

per_person = round(total_bill * (1 + tip / 100) / number_of_people, 2)

print(f"Each person should pay: ${per_person}")