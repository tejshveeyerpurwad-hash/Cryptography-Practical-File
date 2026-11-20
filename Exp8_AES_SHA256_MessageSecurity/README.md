# Experiment 8: AES Encryption and SHA-256 Hashing for Securing Text Messages

## Aim
To implement AES encryption and SHA-256 hashing using Python in VS Code to understand how text messages can be protected and their integrity can be checked.

## Software Used
- VS Code
- Python

## Introduction
AES and SHA-256 are two important techniques used in cybersecurity to protect information.

AES is used to encrypt messages, while SHA-256 is used to generate a hash value to check whether the original message has been changed.

### 1. AES Encryption
AES (Advanced Encryption Standard) is a symmetric encryption algorithm. It uses the same secret key for encryption and decryption.

- It converts readable text into encrypted text.
- It supports 128-bit, 192-bit, and 256-bit keys.
- It is widely used to protect sensitive information.
- The original message can be recovered using the correct key.

### 2. SHA-256 Hashing
SHA-256 (Secure Hash Algorithm 256-bit) is a hashing technique that converts input data into a fixed-length hash value.

- It always generates a 256-bit hash.
- It is a one-way process.
- Even a small change in the message produces a different hash.
- It is commonly used to check data integrity.

## Procedure

1. Open VS Code.
2. Create a new Python file.
3. Install the required Python library for AES encryption.
4. Import the required libraries.
5. Enter a sample text message.
6. Generate a secret key for AES encryption.
7. Encrypt the message using AES.
8. Decrypt the encrypted message using the same secret key.
9. Generate the SHA-256 hash of the original message.
10. Display the encrypted message, decrypted message, and hash value.
11. Compare the original and decrypted messages.
12. Observe how SHA-256 helps check message integrity.

## Working of AES
1. Enter a readable text message.
2. Generate or select a secret encryption key.
3. Encrypt the message using AES.
4. The message is converted into ciphertext.
5. Decrypt the ciphertext using the same secret key.
6. Recover the original message.

## Working of SHA-256
1. Enter the original text message.
2. Pass the message to the SHA-256 algorithm.
3. Generate a fixed-length hash value.
4. Display the generated hash.
5. Change a small part of the message and generate the hash again.
6. Compare both hash values to observe the difference.

## Difference Between AES and SHA-256

| Feature | AES | SHA-256 |
|---|---|---|
| Type | Encryption algorithm | Hashing algorithm |
| Main Purpose | Protects message confidentiality | Checks data integrity |
| Key | Uses a secret key | Does not require a secret key |
| Output | Ciphertext | 256-bit hash |
| Reversible | Yes, with the correct key | No |
| Usage | Secure message encryption | Integrity verification |

## Result
Successfully implemented AES encryption and SHA-256 hashing using Python in VS Code. Encrypted and decrypted a sample text message using AES and generated its SHA-256 hash to understand data protection and integrity checking.

## Conclusion
In this experiment, we learned how AES protects text messages through encryption and decryption. We also learned how SHA-256 generates a unique-looking hash value to check whether data has been modified. Both techniques are important for securing information in modern applications.