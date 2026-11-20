# Cryptography and Network Security — Practical File

**Student:** Tejshvini Yerpurwad
**Roll No:** BETN1AI24043
**Section:** D
**College:** ITM University, Gwalior, Madhya Pradesh
**Course:** Cryptography (CSL0509)
**Programme:** B.Tech AIML, Semester V
**Faculty:** Mr. Hirendra Singh Sengar
**Academic Year:** 2026–27

## Experiments

| No. | Folder | Title | Tool |
|---|---|---|---|
| 1 | Exp1_Caesar_Vigenere_RailFence | Caesar, Vigenere, Rail Fence | CrypTool |
| 2 | Exp2_FrequencyAnalysis | Frequency Analysis | CrypTool |
| 3 | Exp3_DES_AES | DES and AES | CrypTool |
| 4 | Exp4_RSA_OpenSSL | RSA Key Gen & File Enc/Dec | OpenSSL |
| 5 | Exp5_SHA256_DigitalSignature | SHA-256 & Digital Signature | OpenSSL |
| 6 | Exp6_X509_Certificate | Self-Signed X.509 Cert | OpenSSL |
| 7 | Exp7_RSA_DiffieHellman | RSA & Diffie-Hellman | Python/VS Code |
| 8 | Exp8_AES_SHA256_MessageSecurity | AES + SHA-256 | Python/VS Code |
| 9 | Exp9_PasswordHashing_Salting | Password Hashing & Salting | Python/VS Code |
| 10 | Exp10_HTTPS_TLS_Wireshark | HTTPS/TLS Capture | Wireshark |
| 11 | Exp11_VPN_Traffic_Analysis | VPN Traffic Analysis | Wireshark |
| 12 | Exp12_Secure_Insecure_Protocols | Secure vs Insecure Protocols | Wireshark |
| 13 | Exp13_JohnTheRipper_PasswordAudit | Password Auditing | Kali/John |
| 14 | Exp14_SSH_Passwordless_Authentication | SSH Passwordless Auth | Kali/OpenSSH |
| 15 | Exp15_OpenVPN_Configuration | OpenVPN Config | Kali/OpenVPN |
| 16 | Exp16_WPA2_Wireless_Network | WPA2-AES Wireless | Packet Tracer |

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Notes
- OpenSSL not installed in this environment; Exp4-6 require manual OpenSSL commands.
- GUI experiments (1,2,3,10,11,12,15,16) require manual execution.
- Do not commit private keys (see .gitignore).
- Results marked VERIFIED only where actually executed here.
