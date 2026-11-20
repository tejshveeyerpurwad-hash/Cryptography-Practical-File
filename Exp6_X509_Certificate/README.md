# Experiment 6: Creation and Inspection of Self-Signed X.509 Digital Certificates

## Aim
To create and inspect self-signed X.509 digital certificates using OpenSSL and understand their important attributes.

## Software Used
- OpenSSL
- Command Prompt / Terminal

## Introduction
An X.509 certificate is a digital document used to verify the identity of a person, website, or organization.

It contains information about the certificate owner and a public key. Certificates are commonly used in secure communication, such as HTTPS websites.

A self-signed certificate is a certificate that is signed using its own private key instead of being signed by a trusted Certificate Authority (CA).

### Important Certificate Attributes

An X.509 certificate contains several important attributes:

1. **Subject:** Contains information about the certificate owner.
2. **Issuer:** Identifies who issued or signed the certificate.
3. **Public Key:** Contains the public key of the certificate owner.
4. **Serial Number:** A unique number assigned to the certificate.
5. **Validity Period:** Shows the starting and expiration dates of the certificate.
6. **Signature Algorithm:** Specifies the algorithm used to sign the certificate.
7. **Signature:** Used to verify the authenticity of the certificate.

## Procedure

1. Open Command Prompt or Terminal.
2. Check whether OpenSSL is installed.
3. Generate an RSA private key.
4. Create a self-signed X.509 certificate using the private key.
5. Provide the required certificate details, such as country, organization, and common name.
6. Save the generated certificate in PEM format.
7. Use OpenSSL to inspect the certificate details.
8. Observe the subject, issuer, serial number, validity period, and public key.
9. Analyze the certificate attributes.
10. Check whether the certificate is self-signed by comparing its subject and issuer.

## OpenSSL Commands

### Step 1: Generate RSA Private Key

```bash
openssl genpkey -algorithm RSA -out private.key -pkeyopt rsa_keygen_bits:2048
```

### Step 2: Create a Self-Signed X.509 Certificate

```bash
openssl req -new -x509 -key private.key -out certificate.crt -days 365 -sha256
```

Enter the requested certificate information when prompted.

### Step 3: Display Certificate Details

```bash
openssl x509 -in certificate.crt -text -noout
```

### Step 4: Display Certificate Subject

```bash
openssl x509 -in certificate.crt -subject -noout
```

### Step 5: Display Certificate Issuer

```bash
openssl x509 -in certificate.crt -issuer -noout
```

### Step 6: Display Certificate Validity Dates

```bash
openssl x509 -in certificate.crt -dates -noout
```

## Important Files

| File Name | Purpose |
|---|---|
| private.key | Stores the RSA private key |
| certificate.crt | Stores the self-signed X.509 certificate |

## Analysis of Certificate Attributes

After inspecting the certificate, we can understand the following:

- The subject contains the details of the certificate owner.
- The issuer shows who signed the certificate.
- In a self-signed certificate, the subject and issuer are generally the same.
- The validity period tells us when the certificate is valid.
- The public key is included in the certificate.
- The signature algorithm shows how the certificate was signed.

A self-signed certificate is useful for learning and testing, but it is not automatically trusted by browsers or other systems.

## Result
Successfully created a self-signed X.509 digital certificate using OpenSSL. Inspected its important attributes, including subject, issuer, public key, serial number, validity period, and signature algorithm.

## Conclusion
In this experiment, we learned how to generate and inspect self-signed X.509 certificates using OpenSSL. We understood the different certificate attributes and learned how certificates help identify users and systems during secure communication.
