from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(text):
    key = get_random_bytes(32)  # Generate a random 256-bit key
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Pad the text to ensure it's a multiple of the block size (16 bytes)
    padded_text = text + b' ' * (-len(text) % 16)
    
    encrypted_data = cipher.encrypt(padded_text)
    return key, cipher, encrypted_data

def decrypt(key, cipher, encrypted_data):
    decrypted_padded = cipher.decrypt(encrypted_data)
    decrypted_text = decrypted_padded.rstrip(b' ')
    return decrypted_text.decode('utf-8')

text_to_encrypt = "Welcome to Lagos"
key, cipher, encrypted_data = encrypt(text_to_encrypt)

print(f"Encrypted data: {encrypted_data}")
print(f"Decrypted text: {decrypt(key, cipher, encrypted_data)}")