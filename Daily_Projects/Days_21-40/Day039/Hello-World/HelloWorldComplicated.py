import string
import random

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def encrypt_string(text, key):
    encrypted_text = ''
    for i, c in enumerate(text):
        key_c = key[i % len(key)]
        encrypted_c = chr((ord(c) + ord(key_c)) % 256)
        encrypted_text += encrypted_c
    return encrypted_text

def print_hello_world():
    message = "Hello World!"
    key = generate_random_string(len(message))
    encrypted_message = encrypt_string(message, key)
    decrypted_message = encrypt_string(encrypted_message, key)
    print(decrypted_message)

print_hello_world()


# https://learn.microsoft.com/en-us/training/modules/python-object-oriented-programming/media/sort-invoice.png