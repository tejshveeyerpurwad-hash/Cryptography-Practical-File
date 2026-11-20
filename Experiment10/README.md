# Experiment 10: HTTPS Traffic Capture and TLS Handshake Analysis

## Aim
To capture HTTPS traffic using Wireshark and identify the TLS handshake, digital certificates, and cipher suites used during secure communication.

## Software Used
- Wireshark
- Web Browser
- Internet Connection

## Introduction
HTTPS (Hypertext Transfer Protocol Secure) is used to protect communication between a web browser and a web server.

It uses TLS (Transport Layer Security) to encrypt data and protect it from unauthorized access.

Wireshark is a network analysis tool that allows us to capture and inspect network packets. In this experiment, we use Wireshark to observe HTTPS communication and understand how TLS establishes a secure connection.

### 1. TLS Handshake
The TLS handshake is the process through which a client and server establish a secure connection.

During the handshake:
- The client sends a Client Hello message.
- The server responds with a Server Hello message.
- The server provides its digital certificate when required.
- Both sides establish the required cryptographic secrets.
- Secure communication begins after the handshake is completed.

### 2. Digital Certificates
A digital certificate is used to verify the identity of a website or server.

It contains important information such as:
- Website or server name.
- Certificate issuer.
- Public key.
- Validity period.
- Digital signature.

### 3. Cipher Suites
A cipher suite is a collection of cryptographic algorithms used to secure communication.

It defines the algorithms used for key exchange, authentication, encryption, and message integrity.

For example, a TLS 1.2 cipher suite may use AES for encryption and SHA-256 for integrity.

## Procedure

1. Open Wireshark on your computer.
2. Select the active network interface, such as Wi-Fi or Ethernet.
3. Start capturing network traffic.
4. Open a web browser.
5. Visit an HTTPS website.
6. Allow the website to load completely.
7. Return to Wireshark and stop the packet capture.
8. Apply the display filter `tls` to view TLS packets.
9. Find the Client Hello and Server Hello messages.
10. Inspect the certificate information provided by the server.
11. Identify the cipher suites supported and selected during the handshake.
12. Analyze the captured packets and understand how HTTPS communication is secured.

## Useful Wireshark Filters

| Filter | Purpose |
|---|---|
| `tls` | Displays TLS packets |
| `tls.handshake` | Displays TLS handshake packets |
| `tls.handshake.type == 1` | Displays Client Hello messages |
| `tls.handshake.type == 2` | Displays Server Hello messages |
| `tls.handshake.type == 11` | Displays Certificate messages |
| `tcp.port == 443` | Displays TCP traffic using HTTPS port |

Note: Some modern TLS 1.3 connections encrypt certificate messages, so their details may not be visible in an ordinary packet capture.

## TLS Handshake Process

The basic TLS handshake includes the following steps:

1. **Client Hello:** The browser sends supported TLS versions, random values, and cipher suites.
2. **Server Hello:** The server selects the TLS version and cipher suite.
3. **Certificate:** The server provides its digital certificate when required.
4. **Key Exchange:** Both sides establish shared cryptographic secrets.
5. **Finished Messages:** Both sides confirm that the handshake was successful.
6. **Secure Communication:** Encrypted application data is exchanged.

## Analysis

After capturing HTTPS traffic, we can observe the following:

- TLS handshake messages help establish a secure connection.
- Digital certificates help verify the identity of the server.
- Cipher suites define the cryptographic algorithms used for communication.
- HTTPS encrypts application data, making its contents difficult to read directly from captured packets.
- Wireshark helps us understand how secure communication takes place at the network level.

## Result
Successfully captured HTTPS traffic using Wireshark and analyzed TLS handshake messages, digital certificate information, and cipher suites. Understood how TLS helps establish secure communication between a browser and a web server.

## Conclusion
In this experiment, we learned how to capture and analyze HTTPS traffic using Wireshark. We understood the TLS handshake process, the role of digital certificates, and the importance of cipher suites in secure communication. We also learned how TLS protects data exchanged between a client and a server.