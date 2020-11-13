import random
import string

UPPERCASE_CHARS = tuple(string.ascii_uppercase)
LOWERCASE_CHARS = tuple(string.ascii_lowercase)
DIGITS = tuple(string.digits)
SPECIALS = ('!', '@', '#', '$', '%', '^', '&', '*')

def generate_random_password(total, sequences):
    