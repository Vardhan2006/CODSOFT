import random
import string

def generate_password(length, use_uppercase, use_digits, use_punctuation):
    characters = string.ascii_lowercase
    mandatory_characters = []

    if use_uppercase:
        characters += string.ascii_uppercase
        mandatory_characters.append(random.choice(string.ascii_uppercase))
    
    if use_digits:
        characters += string.digits
        mandatory_characters.append(random.choice(string.digits))
    
    if use_punctuation:
        characters += string.punctuation
        mandatory_characters.append(random.choice(string.punctuation))
    
    remaining_length = length - len(mandatory_characters)
    password = mandatory_characters + [random.choice(characters) for _ in range(remaining_length)]
    random.shuffle(password)
    return ''.join(password)

def main():
    print("\n" + "="*45)
    print("       Welcome to Password Generator      ")
    print("="*45 + "\n")
    
    length = int(input("Enter the desired length for the password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_punctuation = input("Include punctuation? (yes/no): ").strip().lower() == 'yes'

    if length < 1:
        print("\nPassword length must be at least 1.")
        return

    password = generate_password(length, use_uppercase, use_digits, use_punctuation)
    
    print("\n" + "="*45)
    print("         Your Generated Password          ")
    print("="*45)
    print(f"\n{password}\n")
    print("="*45)

if __name__ == "__main__":
    main()
