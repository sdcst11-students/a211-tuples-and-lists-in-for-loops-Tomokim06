# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")

q = "Enter a number less than 10: "
a = int(input(q))

if a <= 10:
    print(people[a-1])
else:
    print("Your number was too big")