import random
import string


def generate_random_pass(length):
    """
    Generates a random password.
    :param length: the length of the random password to be generated
    (default is 10)
    :return: generated password
    """
    characters = string.ascii_letters + string.digits + '@$!%*?^&#'
    generated_password = random.choice(
        string.ascii_uppercase
    ) + random.choice(
        '@$!%*?^&#'
    ) + random.choice(string.digits) + ''.join(
        random.choices(characters, k=length - 3)
    )
    password = list(generated_password)
    random.shuffle(password)
    password = ''.join(password).replace(" ", "")
    return password


def generate_random_email(
        domain: str, prefix: str, length: int
):
    """
    Function generates a random email address.

    :param domain: the domain of the email address
    (default is 'yopmail.com')
    :param prefix: the prefix of the email address before the random string
     (default is 'test_n')
    :param length:the length of the random string to be generated
    (default is 6)
    """
    characters = string.ascii_letters + string.digits
    random_string = ''.join(
        random.choice(characters) for _ in range(length)
    )
    email = f"{prefix}{random_string}@{domain}"
    return email
