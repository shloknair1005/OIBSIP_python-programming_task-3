import string
import random

length = int(input("Enter the length of the password: "))
def generate_pass(length):
    if length < 4:
        raise ValueError("Passworrd must be more than 4 characters")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    chars = lowercase + uppercase + digits + symbols
    password += random.choices(chars, k=length-4)

    random.shuffle(password)
    return ''.join(password)

passw = generate_pass(length)
print(f"Generated password: {passw}")
