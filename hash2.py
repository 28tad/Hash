import uuid
import hashlib


def hash_password(password):
    # uuid used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


new_pass = input('Enter your password: ')
hashed_password = hash_password(new_pass)
print('String to store in the database: ' + hashed_password)
old_pass = input('Enter the password again for verification: ')

if check_password(hashed_password, old_pass):
    print('You entered the correct password')
else:
    print('Sorry, but the passwords don not match')
