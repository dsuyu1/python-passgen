import random
import string

def generate_password(min_length: int = 8, max_length: int = 16): # password will always have a different length
    length = random.randint(min_length, max_length)
    # alphabet is a huge list of all ascii letters, digits, and punctuation
    alphabet = string.ascii_letters + string.digits + string.punctuation 
    # picks 10 random letters, digits, and punctuation for our password
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password


def password_strength(password: str): # function accepts one parameter, password
    if len(password) < 8:
        return "Weak"
    # no lower/uppercase letters
    if not any(c.islower() for c in password) or not any (c.isupper() for c in password):
        return "Moderate"
    # no digits or special characters
    if not any(c.isdigit() for c in password) or not any(c in string.punctuation for c in password):
        return "Moderate"
    return "Strong"




password = generate_password()
strength = password_strength(password)

print(f"Generated password: {password}")
print(f"Length of password: {len(password)}")
print(f"Password strength: {strength}")


