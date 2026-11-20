# Cryptography and Network Security — Practical File

**Student:** Tejshvini Yerpurwad
**Roll No:** BETN1AI24043
**Section:** D
**College:** ITM University, Gwalior, Madhya Pradesh
**Course:** Cryptography (CSL0509)
**Programme:** B.Tech AIML, Semester V
**Faculty:** Mr. Hirendra Singh Sengar
**Academic Year:** 2026–27

## About

This repository holds my practical work for the Cryptography and Network Security course. It covers classical ciphers, modern symmetric and asymmetric cryptography, hashing, digital signatures, certificates, network traffic analysis, password security, SSH, VPN and wireless security. Each experiment is in its own folder with a README, code or commands, screenshots and notes.

## Experiment Index

| No. | Folder | Title | Tool |
|---|---|---|---|
| 1 | Exp1_Caesar_Vigenere_RailFence | Caesar, Vigenere and Rail Fence Ciphers | CrypTool |
| 2 | Exp2_FrequencyAnalysis | Frequency Analysis of Classical Ciphers | CrypTool |
| 3 | Exp3_DES_AES | DES and AES Comparison | CrypTool |
| 4 | Exp4_RSA_OpenSSL | RSA Key Generation and File Encryption/Decryption | OpenSSL |
| 5 | Exp5_SHA256_DigitalSignature | SHA-256 Hashing and Digital Signatures | OpenSSL |
| 6 | Exp6_X509_Certificate | Self-Signed X.509 Certificate | OpenSSL |
| 7 | Exp7_RSA_DiffieHellman | RSA and Diffie-Hellman Algorithms | VS Code / Python |
| 8 | Exp8_AES_SHA256_MessageSecurity | AES Encryption and SHA-256 Message Security | VS Code / Python |
| 9 | Exp9_PasswordHashing_Salting | Password Hashing With and Without Salt | VS Code / Python |
| 10 | Exp10_HTTPS_TLS_Wireshark | HTTPS Traffic and TLS Handshake Analysis | Wireshark |
| 11 | Exp11_VPN_Traffic_Analysis | VPN Traffic Analysis | Wireshark |
| 12 | Exp12_Secure_Insecure_Protocols | Secure and Insecure Protocol Analysis | Wireshark |
| 13 | Exp13_JohnTheRipper_PasswordAudit | Password Auditing with John the Ripper | Kali Linux |
| 14 | Exp14_SSH_Passwordless_Authentication | SSH/RSA Key Generation and Passwordless Authentication | Kali Linux |
| 15 | Exp15_OpenVPN_Configuration | Secure VPN Configuration with OpenVPN | Kali Linux |
| 16 | Exp16_WPA2_Wireless_Network | Secure Wireless Network with WPA2-AES | Cisco Packet Tracer |

## Technologies

Python, CrypTool, OpenSSL, Wireshark, Kali Linux, John the Ripper, OpenSSH, OpenVPN, Cisco Packet Tracer.

## Running Python Experiments

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cd Exp7_RSA_DiffieHellman\Codes
python RSA.py
python diffie_hellman.py
```

Experiments 8 and 9 are run similarly from their folders.

## Execution Status

- Verified locally: Experiments 7, 8 and 9 (Python).
- Pending manual execution: 1-6 (OpenSSL not installed here), 10-12 (Wireshark), 13-15 (Kali Linux), 16 (Packet Tracer).
- No screenshots have been fabricated. Genuine capture instructions are in SCREENSHOT_GUIDE.md.

## Repository Layout

```
.
├── Exp1_.../ ... Exp16_.../
├── README.md
├── SCREENSHOT_GUIDE.md
├── FINAL_SUBMISSION_CHECKLIST.md
├── requirements.txt
└── .gitignore
```

## Notes

- Private keys, certificates and captures are ignored by .gitignore.
- Sample data uses harmless test values only.
- Reference material used for structure and wording includes the course lab manual and standard tool documentation.
