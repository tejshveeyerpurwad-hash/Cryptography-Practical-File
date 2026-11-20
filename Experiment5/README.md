# Experiment 5: SHA-256 Hashing and Digital Signature Verification

## Aim
To generate SHA-256 hashes, create digital signatures, and verify the authenticity of digital signatures using OpenSSL.

## Software Used
- OpenSSL
- Command Prompt / Terminal

## Introduction
SHA-256 and Digital Signatures are important techniques used in cybersecurity to protect data and verify its authenticity.

### 1. SHA-256 Hashing
SHA-256 is a hashing algorithm that converts any input data into a fixed-length hash value of 256 bits.

- It generates a unique-looking hash for the given input.
- Even a small change in the original data produces a different hash.
- It is a one-way process, so the original data cannot be recovered from the hash.
- It is commonly used to check data integrity.

### 2. Digital Signature
A digital signature is used to verify the authenticity and integrity of a file.

It uses two keys:
- **Private Key:** Used to create the digital signature.
- **Public Key:** Used to verify the digital signature.

If the file is changed after signing, the signature verification will fail.

## Procedure

1. Open Command Prompt or Terminal.
2. Check whether OpenSSL is installed.
3. Create a sample text file containing a message.
4. Generate the SHA-256 hash of the file.
5. Generate an RSA private key.
6. Extract the public key from the private key.
7. Create a digital signature using the private key.
8. Verify the digital signature using the public key.
9. Modify the original file and perform verification again.
10. Observe the verification result.

## OpenSSL Commands

### Step 1: Create a Sample File

```bash
echo Hello, this is my digital signature practical. > message.txt
```

### Step 2: Generate SHA-256 Hash

```bash
openssl dgst -sha256 message.txt
```

### Step 3: Generate RSA Private Key

```bash
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
```

### Step 4: Generate RSA Public Key

```bash
openssl pkey -in private.pem -pubout -out public.pem
```

### Step 5: Create Digital Signature

```bash
openssl dgst -sha256 -sign private.pem -out signature.bin message.txt
```

### Step 6: Verify Digital Signature

```bash
openssl dgst -sha256 -verify public.pem -signature signature.bin message.txt
```

If the file is unchanged and the correct public key is used, OpenSSL displays:

```text
Verified OK
```

If the file is modified, verification will fail.

## Important Files

| File Name | Purpose |
|---|---|
| message.txt | Contains the original message |
| private.pem | Stores the private key |
| public.pem | Stores the public key |
| signature.bin | Stores the digital signature |

## Result
Successfully generated a SHA-256 hash, created a digital signature using the RSA private key, and verified the signature using the corresponding public key.

## Conclusion
In this experiment, we learned how SHA-256 generates a hash to check data integrity. We also learned how digital signatures work using private and public keys. Signature verification helps confirm that a file has not been changed and that it was signed using the corresponding private key.