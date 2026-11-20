# Experiment 3: Comparison of DES and AES Encryption

## Aim
To compare DES and AES encryption by encrypting sample data and evaluating their security and performance using CrypTool.

## Software Used
- CrypTool

## Introduction
DES and AES are two encryption algorithms used to protect data from unauthorized access.

Both algorithms convert readable data (plaintext) into an unreadable form (ciphertext). The original data can be recovered using the correct decryption key.

### 1. DES (Data Encryption Standard)
DES is a symmetric encryption algorithm, which means the same key is used for encryption and decryption.

- It uses a 56-bit effective key.
- It processes data in 64-bit blocks.
- It uses 16 rounds of encryption.
- DES is now considered insecure because its key size is too small.

### 2. AES (Advanced Encryption Standard)
AES is a modern symmetric encryption algorithm designed to provide better security.

- It supports 128-bit, 192-bit, and 256-bit keys.
- It processes data in 128-bit blocks.
- It uses 10, 12, or 14 rounds depending on the key size.
- AES provides strong security and is widely used today.

## Procedure
1. Open CrypTool software.
2. Enter a sample plaintext message.
3. Select the DES encryption algorithm.
4. Enter the required encryption key.
5. Encrypt the plaintext and observe the ciphertext.
6. Decrypt the ciphertext using the same key.
7. Repeat the same process using the AES algorithm.
8. Enter a suitable AES key and encrypt the same plaintext.
9. Decrypt the AES ciphertext using the same key.
10. Compare the encryption results, security, and performance of both algorithms.

## Comparison Between DES and AES

| Feature | DES | AES |
|---|---|---|
| Full Form | Data Encryption Standard | Advanced Encryption Standard |
| Key Size | 56 bits | 128, 192, 256 bits |
| Block Size | 64 bits | 128 bits |
| Number of Rounds | 16 | 10, 12, 14 |
| Security | Weak by modern standards | Strong |
| Performance | Older and less efficient on modern systems | Generally faster and more efficient |
| Usage | Mostly historical | Widely used today |

## Security Analysis
DES is not considered secure today because its 56-bit key can be cracked using brute-force attacks with modern computing resources.

AES is much stronger because it supports larger key sizes, making brute-force attacks extremely difficult.

## Performance Analysis
Both algorithms can encrypt and decrypt data successfully. AES generally provides better performance on modern systems, especially when hardware acceleration is available.

The actual encryption time may depend on the computer and the amount of data used.

## Result
Successfully performed DES and AES encryption and decryption using CrypTool. Compared both algorithms based on their key size, security, block size, and performance.

## Conclusion
In this experiment, we learned how DES and AES encryption algorithms work. We found that DES has weaker security because of its small key size, while AES provides better security and is widely used in modern applications. Therefore, AES is preferred over DES for protecting sensitive information.