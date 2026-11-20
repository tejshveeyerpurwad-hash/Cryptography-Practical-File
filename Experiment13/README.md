# Experiment 13: Password Auditing Using John the Ripper

## Aim
To perform password auditing using John the Ripper in Kali Linux and evaluate the strength of passwords against password-cracking attacks.

## Software Used
- Kali Linux
- John the Ripper
- Terminal

## Introduction
Password auditing is a process of checking whether passwords are strong enough to protect user accounts from unauthorized access.

John the Ripper is a password security auditing tool used to test password strength. It checks password hashes against different password guesses and helps identify weak passwords.

In this experiment, we use John the Ripper to understand how weak passwords can be identified and why strong passwords are important.

### 1. John the Ripper
John the Ripper is a password auditing tool commonly used by security professionals.

- It checks the strength of password hashes.
- It supports different password hash formats.
- It can use wordlists to test common passwords.
- It helps identify weak and easily guessable passwords.

### 2. Password Strength
Password strength depends on how difficult it is for someone to guess or crack a password.

A strong password generally contains:
- Uppercase letters.
- Lowercase letters.
- Numbers.
- Special characters.
- Sufficient length.

Examples:

- Weak password: `123456`
- Weak password: `password123`
- Stronger password: `R8!mQ2#vL9@p`

## Procedure

1. Open Kali Linux.
2. Open the Terminal.
3. Check whether John the Ripper is installed.
4. Create a test file containing sample password hashes for your own lab.
5. Select the appropriate hash format.
6. Use John the Ripper with a wordlist to audit the test passwords.
7. Observe which passwords are successfully identified.
8. Display the recovered test passwords.
9. Compare weak and strong passwords.
10. Analyze why some passwords are easier to guess than others.

## Useful Commands

### Step 1: Check John the Ripper Version

```bash
john --version
```

### Step 2: View Available Options

```bash
john --help
```

### Step 3: Perform Password Auditing

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

### Step 4: Display Recovered Passwords

```bash
john --show hashes.txt
```

Note: The `rockyou.txt` wordlist may need to be extracted first if it is stored as `rockyou.txt.gz`.

## Important Terms

| Term | Description |
|---|---|
| Password Hash | A converted representation of a password |
| Wordlist | A collection of commonly used password guesses |
| Hash Format | The algorithm or format used to create a password hash |
| Password Cracking | Testing password guesses against stored hashes |
| Password Auditing | Checking whether passwords are strong or weak |

## Analysis

After performing password auditing, we can observe the following:

- Short and common passwords are easier to guess.
- Passwords found in common wordlists can be identified quickly.
- Longer and more complex passwords are generally harder to guess.
- Unique passwords reduce the risk of attacks using leaked credentials.
- Password hashing algorithms and proper salting improve password storage security.

## Result
Successfully performed password auditing using John the Ripper in Kali Linux. Tested sample password hashes, identified weak passwords, and evaluated the importance of using strong passwords.

## Conclusion
In this experiment, we learned how John the Ripper helps identify weak passwords through password auditing. We understood that common and short passwords are more vulnerable to attacks, while longer and unique passwords provide better protection. We also learned the importance of secure password storage and regular password auditing.