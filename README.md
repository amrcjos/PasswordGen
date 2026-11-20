
# PasswordGen 🔐

A secure and customizable password generator built with Python.

PasswordGen uses Python's `secrets` module to generate cryptographically secure passwords, with customizable character sets, entropy estimation and automatic clipboard integration.

## Features

- Cryptographically secure password generation.
- Customizable password length.
- Lowercase and uppercase letters.
- Numbers and special characters.
- Option to disable specific character sets.
- Search-space entropy estimation in bits.
- Automatic clipboard copying.
- Command-line interface (CLI).
- Automated tests with pytest.

## Requirements

- Python 3.10 or higher.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/PasswordGen.git
```

Navigate to the project directory:

```bash
cd PasswordGen
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Generate a password with default settings:

```bash
python genpass.py
```

Generate a 24-character password:

```bash
python genpass.py --length 24
```

Generate a 32-character password without symbols:

```bash
python genpass.py --length 32 --no-symbols
```

Disable numbers and symbols:

```bash
python genpass.py --length 40 --no-digits --no-symbols
```

Generate a password without copying it to the clipboard:

```bash
python genpass.py --length 24 --no-copy
```

Display available options:

```bash
python genpass.py --help
```

## Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

## Technologies

- Python
- secrets
- argparse
- math
- pyperclip
- pytest

## Security

PasswordGen uses Python's `secrets` module instead of the standard `random` module for cryptographically secure random selection.

The entropy calculation estimates the size of the valid password search space. It does not represent the exact Shannon entropy of the generator's output distribution.

