# Experiment 11: VPN Traffic Capture and Analysis

## Aim
To capture and analyze encrypted VPN traffic using Wireshark and compare it with unencrypted network communication.

## Software Used
- Wireshark
- VPN Software
- Internet Connection

## Introduction
A VPN (Virtual Private Network) is a technology that creates a secure connection between a user's device and a VPN server.

It encrypts network traffic so that other people on the network cannot easily read the transmitted data.

Wireshark is a network analysis tool used to capture and inspect network packets. In this experiment, we use Wireshark to observe the differences between encrypted VPN traffic and normal unencrypted network communication.

### 1. VPN Traffic
VPN traffic is protected using encryption. When a device connects to a VPN server, its network data travels through an encrypted tunnel.

- It protects data from being easily read by unauthorized users.
- It hides the contents of traffic from local network observers.
- It provides a secure connection between the device and VPN server.
- The traffic may use protocols such as OpenVPN or WireGuard.

### 2. Unencrypted Network Communication
Unencrypted communication sends data without encryption.

- Data may be visible in packet captures.
- Information can be read more easily by network observers.
- It does not provide the same confidentiality as encrypted communication.
- HTTP is an example of an unencrypted application protocol.

## Procedure

1. Open Wireshark on your computer.
2. Select the active network interface, such as Wi-Fi or Ethernet.
3. Start capturing network traffic without connecting to a VPN.
4. Visit a website or generate some normal network traffic.
5. Stop the capture and save the packets.
6. Connect to a VPN using VPN software.
7. Start a new capture in Wireshark.
8. Visit a website or generate network traffic while the VPN is connected.
9. Stop the capture and save the VPN traffic.
10. Compare both packet captures.
11. Observe the protocols, packet information, and visibility of transmitted data.
12. Analyze how VPN encryption protects network communication.

## Useful Wireshark Filters

| Filter | Purpose |
|---|---|
| `http` | Displays HTTP traffic |
| `tls` | Displays TLS traffic |
| `dns` | Displays DNS packets |
| `tcp` | Displays TCP packets |
| `udp` | Displays UDP packets |
| `ip.addr == IP_ADDRESS` | Displays packets related to a particular IP address |

Note: VPN traffic filters depend on the VPN protocol being used. For example, OpenVPN commonly uses UDP or TCP, while WireGuard commonly uses UDP.

## Comparison Between VPN and Unencrypted Traffic

| Feature | VPN Traffic | Unencrypted Traffic |
|---|---|---|
| Encryption | Encrypted tunnel | May be unencrypted |
| Data Visibility | Contents are protected | Contents may be readable |
| Privacy | Better protection on local networks | Less protection |
| Packet Analysis | Shows encrypted tunnel traffic | May show readable application data |
| Security | Provides confidentiality | Does not provide confidentiality by itself |

## Analysis

After capturing both types of network traffic, we can observe the following:

- Normal unencrypted HTTP traffic may reveal readable information in Wireshark.
- VPN traffic generally shows encrypted packets between the device and VPN server.
- The destination IP address of the VPN server may be visible.
- Packet size, timing, and traffic volume may still be observable.
- VPN encryption protects the contents of the traffic but does not make all network activity invisible.

## Result
Successfully captured and analyzed VPN traffic and normal network communication using Wireshark. Compared their packet information and observed how VPN encryption protects transmitted data.

## Conclusion
In this experiment, we learned how VPN technology protects network communication through encryption. We used Wireshark to compare VPN traffic with normal unencrypted traffic and understood the differences in data visibility, privacy, and security. We also learned that VPN encryption makes it difficult for network observers to read the actual contents of transmitted data.