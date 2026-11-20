# Experiment 12: Analysis of Secure and Insecure Network Communication Protocols

## Aim
To analyze network packets using Wireshark and identify secure and insecure communication protocols.

## Software Used
- Wireshark
- Internet Connection
- Web Browser

## Introduction
Network protocols are rules that allow devices to communicate and exchange data over a network.

Some protocols provide encryption to protect information, while others transmit data without encryption.

Wireshark is a network analysis tool that helps us capture and inspect network packets. In this experiment, we use Wireshark to identify different network protocols and understand which ones provide secure communication.

### 1. Secure Communication Protocols
Secure protocols use encryption and other security techniques to protect transmitted information.

Examples:

- **HTTPS:** Protects website communication using TLS encryption.
- **SSH:** Provides secure remote access to another computer.
- **SFTP:** Transfers files securely over SSH.
- **TLS:** Provides encryption and authentication for network communication.

### 2. Insecure Communication Protocols
Insecure protocols generally transmit data without encryption, making the information easier to read during packet analysis.

Examples:

- **HTTP:** Transfers website data without encryption.
- **FTP:** Transfers files without built-in encryption.
- **Telnet:** Provides remote access without encrypting the communication.
- **POP3:** Basic POP3 communication does not encrypt data unless TLS is used.

## Procedure

1. Open Wireshark on your computer.
2. Select the active network interface, such as Wi-Fi or Ethernet.
3. Start capturing network packets.
4. Generate network traffic by visiting different websites.
5. Use an HTTP website or a permitted local test environment to observe unencrypted communication.
6. Visit HTTPS websites to observe encrypted communication.
7. Apply display filters to identify different protocols.
8. Select individual packets and inspect their details.
9. Observe whether the application data is readable or encrypted.
10. Compare secure and insecure communication protocols.
11. Record your observations and identify the security differences.

## Useful Wireshark Filters

| Filter | Purpose |
|---|---|
| `http` | Displays HTTP packets |
| `tls` | Displays TLS packets |
| `ssh` | Displays SSH packets |
| `ftp` | Displays FTP packets |
| `telnet` | Displays Telnet packets |
| `dns` | Displays DNS packets |
| `tcp` | Displays TCP packets |
| `udp` | Displays UDP packets |

## Comparison Between Secure and Insecure Protocols

| Feature | Secure Protocols | Insecure Protocols |
|---|---|---|
| Encryption | Uses encryption | Usually no encryption |
| Data Protection | Better protection | Less protection |
| Privacy | Protects data contents | Data may be readable |
| Examples | HTTPS, SSH, SFTP | HTTP, FTP, Telnet |
| Security | More secure | Less secure |

## Analysis

After capturing and analyzing network packets, we can observe the following:

- HTTP packets may contain readable website information.
- HTTPS traffic protects application data using TLS encryption.
- SSH provides encrypted remote communication.
- FTP and Telnet can expose transmitted information because they do not provide encryption by default.
- Wireshark helps identify protocols by examining packet headers and protocol details.
- Encryption makes it difficult to read the actual contents of transmitted data.

## Result
Successfully captured and analyzed network packets using Wireshark. Identified secure and insecure communication protocols and compared their encryption, data visibility, and security features.

## Conclusion
In this experiment, we learned how to analyze network packets using Wireshark. We understood the difference between secure and insecure communication protocols. We also learned that protocols such as HTTPS and SSH protect data using encryption, while protocols such as HTTP, FTP, and Telnet can expose information during communication.