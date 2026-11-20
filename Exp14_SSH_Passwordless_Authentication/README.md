# Experiment 14: SSH Key Generation and Passwordless Authentication

## Aim
To generate SSH/RSA key pairs and configure passwordless authentication between Linux systems using Kali Linux.

## Software Used
- Kali Linux
- OpenSSH
- Terminal
- Two Linux systems or virtual machines

## Introduction
SSH (Secure Shell) is a network protocol used to connect securely to another computer over a network.

It allows users to access remote systems, execute commands, and transfer files securely.

SSH uses encryption to protect communication between two systems.

### 1. SSH Key Generation
SSH key authentication uses two keys:

- **Public Key:** Can be shared with other systems.
- **Private Key:** Must be kept secret on the user's computer.

These keys work together to verify the identity of a user.

### 2. Passwordless Authentication
Passwordless authentication allows a user to connect to another Linux system without entering the account password every time.

It works by placing the user's public key on the remote system. The remote system checks the key using the corresponding private key.

## Procedure

1. Open Kali Linux.
2. Open the Terminal.
3. Check whether OpenSSH is installed.
4. Generate an RSA key pair using the `ssh-keygen` command.
5. Enter a file name for the key pair or use the default location.
6. Set a passphrase if required.
7. Copy the public key to the remote Linux system.
8. Make sure the SSH service is running on the remote system.
9. Connect to the remote system using SSH.
10. Verify that authentication works without entering the remote account password.
11. Test the connection again to confirm successful passwordless authentication.

## Useful Commands

### Step 1: Check SSH Version

```bash
ssh -V
```

### Step 2: Generate RSA Key Pair

```bash
ssh-keygen -t rsa -b 4096
```

Press Enter to use the default file location. You can set a passphrase for additional protection.

### Step 3: Start SSH Service

```bash
sudo systemctl start ssh
```

### Step 4: Enable SSH Service

```bash
sudo systemctl enable ssh
```

### Step 5: Copy Public Key to Remote System

```bash
ssh-copy-id username@remote_ip
```

Replace `username` with the remote Linux username and `remote_ip` with its IP address.

### Step 6: Connect to Remote System

```bash
ssh username@remote_ip
```

If everything is configured correctly, you should be able to connect without entering the remote account password.

## Important Files

| File Name | Purpose |
|---|---|
| id_rsa | Stores the private RSA key |
| id_rsa.pub | Stores the public RSA key |
| authorized_keys | Stores public keys allowed to access the remote account |
| known_hosts | Stores information about previously connected SSH servers |

## Working of SSH Authentication

1. The user generates a public and private key pair.
2. The public key is copied to the remote Linux system.
3. The user requests an SSH connection.
4. The remote system checks whether the public key is authorized.
5. The client proves possession of the corresponding private key.
6. The remote system verifies the authentication.
7. A secure SSH connection is established without requiring the remote account password.

## Result
Successfully generated SSH/RSA public and private key pairs and configured passwordless authentication between Linux systems. Verified the connection using SSH without entering the remote account password.

## Conclusion
In this experiment, we learned how to generate SSH keys and configure passwordless authentication between Linux systems. We understood the role of public and private keys and how SSH provides secure remote access through key-based authentication.