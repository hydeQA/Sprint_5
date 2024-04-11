import random
import string
def user_email_generator():
    user_email = {'email': str(random.choice(string.ascii_letters)) * 3 + str(random.randint(100, 999)) + '@ya.ru'}
    return user_email