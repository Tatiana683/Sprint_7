import random
import string

class RandomCred:
    def generate_login():
        name = "test_user_"
        login = f'{name}{random.randint(1, 999)}'
        return login

    def generate_password():
        password = f'{random.randint(1000, 999999)}'
        return password

    def generate_name():
        length = 9
        all_symbols = string.ascii_uppercase
        first_name = ''.join(random.choice(all_symbols) for _ in range(length))
        return first_name