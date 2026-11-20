
import math
import string
import pytest

from genpass import generate_password, calculate_entropy


# =========================================================
# PASSWORD GENERATION TESTS
# =========================================================

def test_password_length():
    password = generate_password(24)

    assert len(password) == 24


def test_password_minimum_length():
    password = generate_password(8)

    assert len(password) == 8


def test_password_rejects_short_length():
    with pytest.raises(ValueError):
        generate_password(7)


def test_password_contains_lowercase():
    password = generate_password(24)

    assert any(char.islower() for char in password)


def test_password_contains_uppercase():
    password = generate_password(24)

    assert any(char.isupper() for char in password)


def test_password_contains_digit():
    password = generate_password(24)

    assert any(char.isdigit() for char in password)


def test_password_contains_symbol():
    password = generate_password(24)

    assert any(char in string.punctuation for char in password)


# =========================================================
# CHARACTER CUSTOMIZATION TESTS
# =========================================================

def test_password_without_symbols():
    password = generate_password(24, symbols=False)

    assert all(char not in string.punctuation for char in password)


def test_password_without_uppercase():
    password = generate_password(24, uppercase=False)

    assert not any(char.isupper() for char in password)


def test_password_without_digits():
    password = generate_password(24, digits=False)

    assert not any(char.isdigit() for char in password)


def test_password_without_lowercase():
    password = generate_password(24, lowercase=False)

    assert not any(char.islower() for char in password)


def test_password_only_lowercase():
    password = generate_password(
        24,
        lowercase=True,
        uppercase=False,
        digits=False,
        symbols=False
    )

    assert all(char in string.ascii_lowercase for char in password)


def test_password_no_character_types():
    with pytest.raises(ValueError):
        generate_password(
            24,
            lowercase=False,
            uppercase=False,
            digits=False,
            symbols=False
        )


# =========================================================
# ENTROPY TESTS
# =========================================================

def test_entropy_calculation():
    entropy = calculate_entropy(24)

    assert entropy > 0


def test_entropy_increases_with_length():
    short = calculate_entropy(12)
    long = calculate_entropy(24)

    assert long > short



def test_entropy_without_symbols():
    entropy = calculate_entropy(24, symbols=False)

    expected_count = (
        62**24
        - 36**24
        - 36**24
        - 52**24
        + 10**24
        + 26**24
        + 26**24
    )

    expected = math.log2(expected_count)

    assert entropy == pytest.approx(expected)



def test_entropy_no_character_types():
    with pytest.raises(ValueError):
        calculate_entropy(
            24,
            lowercase=False,
            uppercase=False,
            digits=False,
            symbols=False
        )


def test_entropy_rejects_zero_length():
    with pytest.raises(ValueError):
        calculate_entropy(0)


def test_entropy_rejects_negative_length():
    with pytest.raises(ValueError):
        calculate_entropy(-5)

def test_entropy_with_only_lowercase():
    entropy = calculate_entropy(
        24,
        lowercase=True,
        uppercase=False,
        digits=False,
        symbols=False
    )

    expected = 24 * math.log2(26)

    assert entropy == pytest.approx(expected)
