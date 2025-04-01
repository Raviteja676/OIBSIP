import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    char_types = {
        'letters': (string.ascii_letters, use_letters),
        'numbers': (string.digits, use_numbers),
        'symbols': (string.punctuation, use_symbols)
    }

    selected_char_sets = [chars for chars, use in char_types.values() if use]
    
    if not selected_char_sets:
        return "No character types selected. Please try again."
    
    password = [random.choice(chars) for chars in selected_char_sets]
    
    all_chars = ''.join(selected_char_sets)
    password.extend(random.choices(all_chars, k=length - len(password)))
    
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired length of the password: "))
    use_letters = input("Include letters (y/n)? ").strip().lower() == 'y'
    use_numbers = input("Include numbers (y/n)? ").strip().lower() == 'y'
    use_symbols = input("Include symbols (y/n)? ").strip().lower() == 'y'
    
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print("Generated Password:", password)

if _name_ == "_main_":
    main()
