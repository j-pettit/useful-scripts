import random
import secrets
import string

UPPERCASE_CHARS = tuple(string.ascii_uppercase)
LOWERCASE_CHARS = tuple(string.ascii_lowercase)
DIGITS = tuple(string.digits)
SPECIALS = ('!', '@', '#', '$', '%', '^', '&', '*')

SEQUENCE = (UPPERCASE_CHARS,
            LOWERCASE_CHARS,
            DIGITS,
            SPECIALS,
            )

def generate_random_password(total, sequences):
    r = _generate_random_number_for_each_sequence(total, len(sequences))
    print(r)
    password = []


def _generate_random_number_for_each_sequence(total, sequence_number):
    curr_total = 0
    r = []
    for n in range(sequence_number-1, 0, -1):
        curr = random.randint(1, total - curr_total - n)
        curr_total += curr
        r.append(curr)
    r.append(total-sum(r))
    random.shuffle(r)
    return r

generate_random_password(random.randint(6, 20), SEQUENCE)