import random
import string

# Adding all characters to separate lists
lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
special_char = list(string.punctuation)

while True:

# Validating user input using try-except block
    try:

    # Prompting user to enter a number
        pass_len = int(input("How long would you like your password to be?"))

        # User validation - user needs to enter at least 8 characters
        if pass_len < 8:

            print("Your password should be at least 8 characters long!")
            continue

        else:

            print(f"Your password will be {pass_len} characters long.")
            break

    except ValueError as e:
        print(f"Error: {e}. Please try again using a number.")
    

# Shuffling all the lists
random.shuffle(lower_letters)
random.shuffle(upper_letters)
random.shuffle(numbers)
random.shuffle(special_char)

# Calculating percentage of numbers of characters for a strong password
# 60% letters and 40 % numbers + special characters
sixty = round(pass_len * (30/100))
forty = round(pass_len * (20/100))

password = []

# Adding letters to the password
for chars in range(sixty):

    password.append(lower_letters[chars])
    password.append(upper_letters[chars])

# Adding numbers + special characters to the password
for chars in range(forty):
    
    password.append(numbers[chars])
    password.append(special_char[chars])


# Shuffling the password
random.shuffle(password)

# Ensuring password has the right length if user inputs odd number
if pass_len % 2 == 1:
    password.pop()

# Generating the password
result = "".join(password)
print(f"Your generated password is: {result}")
