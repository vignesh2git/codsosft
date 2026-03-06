# Password Generator Application

import random
import string

print("===== PASSWORD GENERATOR =====")
try:
    length = int(input("\nEnter the desired password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    print("Generated Password:", password)

except ValueError:
    print("Invalid input. Please enter numeric values.")