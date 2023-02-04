import string
from random import choice

def generate_short_id(num_of_chars):
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(num_of_chars))
