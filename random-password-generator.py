#random password generator
import string
import secrets

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))

print("Welcome to the Random Password Generator!")
leng = int(input("Entire desired password length (default is 12): ") or 12)
password = generate_password(leng)
print(f"Your password is: {password}")
    
