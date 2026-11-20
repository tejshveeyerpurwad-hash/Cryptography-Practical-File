# Experiment 4: RSA Key Generation and File Encryption/Decryption

## Aim
To generate RSA public and private key pairs using OpenSSL and perform file encryption and decryption.

## Software Used
- OpenSSL
- Command Prompt / Terminal

## Introduction
RSA is an asymmetric encryption algorithm used to secure data. It uses two different keys: a public key and a private key.

The public key is used for encryption, while the private key is used for decryption.

RSA helps protect confidential information and is commonly used in secure communication.

### 1. Public Key
- It can be shared with other people.
- It is used to encrypt data.
- It helps keep information secure.

### 2. Private Key
- It must be kept secret.
- It is used to decrypt data.
- It helps recover the original information.

## Procedure

1. Open Command Prompt or Terminal.
2. Check whether OpenSSL is installed.
3. Generate an RSA private key using OpenSSL.
4. Extract the public key from the private key.
5. Create a sample text file containing a message.
6. Use the public key to encrypt the file.
7. Save the encrypted data into a separate file.
8. Use the private key to decrypt the encrypted file.
9. Open the decrypted file and check the original message.
10. Compare the original file with the decrypted file.

## OpenSSL Commands

### Step 1: Generate RSA Private Key

```bash
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
```

### Step 2: Generate RSA Public Key

```bash
openssl pkey -in private.pem -pubout -out public.pem
```

### Step 3: Create a Sample File

```bash
echo Hello, this is my RSA practical. > message.txt
```

### Step 4: Encrypt the File

```bash
openssl pkeyutl -encrypt -pubin -inkey public.pem -in message.txt -out encrypted.bin
```

### Step 5: Decrypt the File

```bash
openssl pkeyutl -decrypt -inkey private.pem -in encrypted.bin -out decrypted.txt
```

### Step 6: View the Decrypted Message

```bash
type decrypted.txt
```

## Important Files

| File Name | Purpose |
|---|---|
| private.pem | Stores the RSA private key |
| public.pem | Stores the RSA public key |
| message.txt | Contains the original message |
| encrypted.bin | Contains encrypted data |
| decrypted.txt | Contains the decrypted message |

## Result
Successfully generated RSA public and private key pairs using OpenSSL. Encrypted a sample file using the public key and decrypted it using the private key. The original message was recovered successfully.

## Conclusion
In this experiment, we learned how RSA encryption works using public and private keys. We generated key pairs and performed encryption and decryption using OpenSSL. We also understood how RSA helps protect confidential information.