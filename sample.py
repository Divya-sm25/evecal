from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_data):
    iv = encrypted_data[:AES.block_size]
    ciphertext = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message

# Example usage:
key = get_random_bytes(16)  # Generate a random 128-bit key
message = b"Hello, this is a secret message!"

# Encrypt the message
encrypted_data = encrypt_message(key, message)
print("Encrypted:", encrypted_data)

# Decrypt the encrypted data
decrypted_message = decrypt_message(key, encrypted_data)
print("Decrypted:", decrypted_message.decode())