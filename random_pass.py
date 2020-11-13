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
    password = []
    for population, k in zip(sequences, r):
        n = 0
        while n < k:
            password += secrets.choice(population)
            n += 1
    random.shuffle(password)

    while _is_repeating(password):
        random.shuffle(password)

    return ''.join(password)

def _generate_random_number_for_each_sequence(total, length):
    ''' Create a random sequence of $length elements with a sum of $total ''' 
    curr_total = 0
    r = []
    for n in range(length-1, 0, -1):
        curr = random.randint(1, total - curr_total - n)
        curr_total += curr
        r.append(curr)
    r.append(total-sum(r))
    random.shuffle(r)
    return r

def _is_repeating(password):
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            return True
        return False

print(generate_random_password(random.randint(6, 6), SEQUENCE))