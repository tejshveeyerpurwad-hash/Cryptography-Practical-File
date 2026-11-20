import os
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Original Message
message = 'Hello BTech Students'
message_bytes = message.encode('utf-8')

# Generate a 128-bit AES key
secret_key = AESGCM.generate_key(bit_length=128)
aes = AESGCM(secret_key)

# Generate a 12-byte nonce
nonce = os.urandom(12)

# Encrypt the message
encrypted_bytes = aes.encrypt(nonce, message_bytes, None)

# Convert encrypted data to Base64 text
encrypted_message = base64.b64encode(
    nonce + encrypted_bytes
).decode('utf-8')

# Decrypt the message
decrypted_bytes = aes.decrypt(nonce, encrypted_bytes, None)
decrypted_message = decrypted_bytes.decode('utf-8')

# SHA-256 Hashing
hash_value = hashlib.sha256(message_bytes).hexdigest()

# Display Results
print("Original Message:", message)

print("\nAES Encryption")
print("Encrypted Text:", encrypted_message)
print("Decrypted Text:", decrypted_message)

print("\nSHA-256 Hashing")
print("SHA-256:", hash_value)
