# Experiment 15: Secure VPN Configuration Using OpenVPN in Kali Linux

## Aim
To configure a secure VPN using OpenVPN in Kali Linux and verify encrypted communication between connected systems.

## Software Used
- Kali Linux
- OpenVPN
- OpenSSL (for PKI)
- Two Linux systems/VMs

## Theory
OpenVPN creates an encrypted tunnel (typically UDP 1194) using TLS for control channel and a symmetric cipher (e.g. AES-256-GCM) for data. A PKI (CA, server cert, client cert) provides authentication.

## Procedure
1. Install OpenVPN and easy-rsa on Kali.
2. Build PKI: CA, server cert/key, client cert/key, DH params, TLS-auth key.
3. Configure server (/etc/openvpn/server.conf) and client (.ovpn).
4. Start OpenVPN service; connect client.
5. Verify tunnel interface (tun0) and ping across tunnel.
6. Capture traffic with Wireshark to confirm encryption.

## Commands (Kali)
```bash
sudo apt update
sudo apt install -y openvpn easy-rsa
make-cadir ~/openvpn-ca && cd ~/openvpn-ca
./easyrsa init-pki
./easyrsa build-ca nopass
./easyrsa gen-req server nopass
./easyrsa sign-req server server
./easyrsa gen-dh
openvpn --genkey --secret ta.key
sudo cp pki/ca.crt pki/issued/server.crt pki/private/server.key pki/dh.pem ta.key /etc/openvpn/
sudo systemctl start openvpn@server
sudo systemctl enable openvpn@server
```

## Expected Output
- tun0 interface up with 10.8.0.1/24.
- Client receives 10.8.0.x and can ping 10.8.0.1.
- Wireshark shows encrypted UDP traffic; no plaintext payload.

## Observations
REQUIRES ADDITIONAL SOFTWARE/HARDWARE (Kali VM + second host). Not verified in this environment.

## Conclusion
OpenVPN provides encrypted site-to-site/remote-access tunnels using TLS + AES; verified only via manual setup.
