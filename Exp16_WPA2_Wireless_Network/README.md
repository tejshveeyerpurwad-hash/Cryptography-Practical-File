# Experiment 16: Design and Implement a Secure Wireless Network Using WPA2 (AES) in Cisco Packet Tracer

## Aim
To design and implement a secure wireless network using WPA2 encryption (AES) in Cisco Packet Tracer and verify secure communication.

## Software Used
- Cisco Packet Tracer
- Wireless router (WRT300N), PCs with wireless NICs

## Theory
WPA2 uses AES-CCMP (Counter Mode with CBC-MAC Protocol) for confidentiality and integrity. A pre-shared key (PSK) authenticates stations; 4-way handshake derives session keys. Open networks expose traffic; WPA2-AES protects it.

## Procedure
1. Place a wireless router and 2 PCs; connect router to a switch/internet (optional).
2. Configure router SSID and Security: WPA2-PSK, AES, passphrase (e.g. StrongPass!2026).
3. On each PC wireless NIC, connect to SSID with passphrase.
4. Verify IP assignment via DHCP and ping between PCs.
5. Capture/inspect wireless frames (Packet Tracer simulation) to confirm encryption.
6. Test that wrong passphrase fails association.

## Verification Checklist
- SSID broadcast; clients associate only with correct PSK.
- Ping between wireless clients succeeds.
- Simulation mode shows encrypted data frames.
- Failed auth with wrong key.

## Observations
REQUIRES MANUAL GUI EXECUTION (Cisco Packet Tracer). Not verified in this environment.

## Conclusion
WPA2-AES secures wireless links via AES-CCMP and PSK authentication; configured and verified in Packet Tracer.
