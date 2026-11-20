import hashlib
import secrets
import hmac
# Password input
password = input("Enter your password: ")
password_bytes = password.encode('utf-8')
# ---------------- WITHOUT SALT ----------------
print("\n--- Password Hashing Without Salt ---")
unsalted_hash = hashlib.sha256(password_bytes).hexdigest()
print("Original Password:", password)
print("SHA-256 Hash:", unsalted_hash)
# ---------------- WITH SALT ----------------
print("\n--- Password Hashing With Salt ---")
# Generate a random 16-byte salt
salt = secrets.token_bytes(16)
# Apply PBKDF2-HMAC-SHA256
salted_hash = hashlib.pbkdf2_hmac(
    'sha256',
    password_bytes,
    salt,
    600000
)
print("Salt:", salt.hex())
print("Salted Hash:", salted_hash.hex())
# ---------------- VERIFICATION ----------------
print("\n--- Password Verification ---")
entered_password = input("Re-enter your password: ")
# Verify unsalted password
check_hash = hashlib.sha256(
    entered_password.encode('utf-8')
).hexdigest()
if hmac.compare_digest(unsalted_hash, check_hash):
    print("Without Salt: Password matched!")
else:
    print("Without Salt: Password did not match!")
# Verify salted password using the same salt
check_salted_hash = hashlib.pbkdf2_hmac(
    'sha256',
    entered_password.encode('utf-8'),
    salt,
    600000
)
if hmac.compare_digest(salted_hash, check_salted_hash):
    print("With Salt: Password matched!")
else:
    print("With Salt: Password did not match!")