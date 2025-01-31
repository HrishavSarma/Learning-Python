# Python Encryption Program
import random
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters   
chars = list(chars)

key = chars.copy()
random.shuffle(key)

#Encrypt
plain_text = input("Enter message to encrypt: ")
encrypted = ""
for letter in plain_text:
    index = chars.index(letter)
    encrypted += key[index]

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {encrypted}")

#Decrypt

encrypted = input("Enter encrypted message: ").replace(" ", "")
decrypt_text = ""

for letter in encrypted:
    index = key.index(letter)
    decrypt_text += chars[index]

print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypt_text}")