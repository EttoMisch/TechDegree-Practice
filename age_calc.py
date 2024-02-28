# Step 1
# Ask the user for their name and the year they were born.
name = input("What is your name?  ")

while True:
    birth_year = input("What year were you born, {}?  ".format(name))
    try:
        birth_year = int(birth_year)
    except ValueError:
        continue 
    else:
        break

# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.
current_year = 2024
current_age = current_year - birth_year 

milestone1 = current_year + (25-current_age)
milestone2 = current_year + (50-current_age)
milestone3 = current_year + (75-current_age)
milestone4 = current_year + (100-current_age)

if current_age < 25:
    print("You will be 25 in {}.".format(milestone1))
if current_age < 50:
    print("You will be 50 in {}.".format(milestone2))
if current_age < 75:
    print("You will be 50 in {}.".format(milestone3))
if current_age < 100:
    print("You will be 50 in {}.".format(milestone4))

# Step 3
# If they're already past any of these ages, skip them.
