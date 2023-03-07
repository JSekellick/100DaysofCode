# Ceasar cipher encode or decode
# Jared Sekellick

def caesar_cipher(message, shift):
    cipher_text = ""
    for char in message:
        if char.isalpha():
            ascii_code = ord(char)
            shifted_ascii_code = ascii_code + shift
            if char.isupper():
                if shifted_ascii_code > ord('Z'):
                    shifted_ascii_code -= 26
                elif shifted_ascii_code < ord('A'):
                    shifted_ascii_code += 26
            else:
                if shifted_ascii_code > ord('z'):
                    shifted_ascii_code -= 26
                elif shifted_ascii_code < ord('a'):
                    shifted_ascii_code += 26
            cipher_text += chr(shifted_ascii_code)
        else:
            cipher_text += char
    return cipher_text

def encrypt_message():
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)
    return encrypted_message

def decrypt_message():
    message = input("Enter the message to decrypt: ")
    shift = int(input("Enter the shift value: "))
    decrypted_message = caesar_cipher(message, -shift)
    print("Decrypted message:", decrypted_message)
    return decrypted_message

mode = input("Do you want to encrypt or decrypt? ")
if mode == "encrypt":
    encrypt_message()
elif mode == "decrypt":
    decrypt_message()
else:
    print("Invalid mode entered. Please enter 'encrypt' or 'decrypt'.")