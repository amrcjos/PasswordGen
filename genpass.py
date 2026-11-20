
import argparse
import math
import secrets
import string
import pyperclip
from itertools import combinations


# =========================================================
# PASSWORD GENERATOR
# =========================================================

def generate_password(
    length=16,
    lowercase=True,
    uppercase=True,
    digits=True,
    symbols=True
):
    if length < 8:
        raise ValueError("Password must have at least 8 characters.")

    character_pools = []

    if lowercase:
        character_pools.append(string.ascii_lowercase)

    if uppercase:
        character_pools.append(string.ascii_uppercase)

    if digits:
        character_pools.append(string.digits)

    if symbols:
        character_pools.append(string.punctuation)

    if not character_pools:
        raise ValueError("At least one character type must be selected.")

    if length < len(character_pools):
        raise ValueError("Password length is too short for selected character types.")

    characters = "".join(character_pools)

    password = [
        secrets.choice(pool)
        for pool in character_pools
    ]

    password += [
        secrets.choice(characters)
        for _ in range(length - len(password))
    ]

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# =========================================================
# ENTROPY CALCULATOR
# =========================================================


def calculate_entropy(
    length,
    lowercase=True,
    uppercase=True,
    digits=True,
    symbols=True
):
    if length < 8:
        raise ValueError("Password must have at least 8 characters.")

    character_pools = []

    if lowercase:
        character_pools.append(string.ascii_lowercase)

    if uppercase:
        character_pools.append(string.ascii_uppercase)

    if digits:
        character_pools.append(string.digits)

    if symbols:
        character_pools.append(string.punctuation)

    if not character_pools:
        raise ValueError("At least one character type must be selected.")

    if length < len(character_pools):
        raise ValueError("Password length is too short for selected character types.")

    alphabet_size = sum(len(pool) for pool in character_pools)

    valid_passwords = 0

    for subset_size in range(len(character_pools) + 1):
        for subset in combinations(character_pools, subset_size):

            excluded_characters = sum(len(pool) for pool in subset)

            remaining_characters = alphabet_size - excluded_characters

            count = remaining_characters ** length

            if subset_size % 2 == 0:
                valid_passwords += count
            else:
                valid_passwords -= count

    if valid_passwords <= 0:
        raise ValueError("No valid passwords can be generated.")

    return math.log2(valid_passwords)



# =========================================================
# COMMAND LINE INTERFACE
# =========================================================

def main():

    parser = argparse.ArgumentParser(
        description="PasswordGen - Secure Password Generator"
    )

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=16,
        help="Password length (default: 16)"
    )

    parser.add_argument(
        "--no-lowercase",
        action="store_false",
        dest="lowercase",
        help="Disable lowercase letters"
    )

    parser.add_argument(
        "--no-uppercase",
        action="store_false",
        dest="uppercase",
        help="Disable uppercase letters"
    )

    parser.add_argument(
        "--no-digits",
        action="store_false",
        dest="digits",
        help="Disable numbers"
    )

    parser.add_argument(
        "--no-symbols",
        action="store_false",
        dest="symbols",
        help="Disable symbols"
    )

    parser.add_argument(
        "--no-copy",
        action="store_true",
        help="Disable automatic password copying"
    )

    args = parser.parse_args()

    try:

        password = generate_password(
            length=args.length,
            lowercase=args.lowercase,
            uppercase=args.uppercase,
            digits=args.digits,
            symbols=args.symbols
        )

        entropy = calculate_entropy(
            length=args.length,
            lowercase=args.lowercase,
            uppercase=args.uppercase,
            digits=args.digits,
            symbols=args.symbols
        )

        print("\nGenerated password:", password)
        print("Password length:", len(password))
        print(f"Estimated entropy: {entropy:.2f} bits")

        if not args.no_copy:

            try:
                pyperclip.copy(password)
                print("Password copied to clipboard!")

            except pyperclip.PyperclipException:
                print("Warning: Could not copy password to clipboard.")

        print()

    except ValueError as error:
        parser.error(str(error))


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()
