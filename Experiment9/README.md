# Experiment 9: Password Hashing With and Without Salting

## Aim
To implement password hashing with and without salting using Python in VS Code and compare their resistance against password attacks.

## Software Used
- VS Code
- Python

## Introduction
Password hashing is a technique used to store passwords securely. Instead of saving the original password, a hash value is stored in the system.

When a user enters a password, the system hashes it and compares the result with the stored hash.

In this experiment, we study two methods of password hashing.

### 1. Password Hashing Without Salt
In this method, the password is directly converted into a hash value using a hashing algorithm such as SHA-256.

- The same password always produces the same hash.
- It is simple to implement.
- Attackers can use precomputed hash tables to guess passwords.
- Users with the same password will have the same hash.

### 2. Password Hashing With Salt
A salt is a random value added to a password before hashing.

- A random salt is generated for each password.
- The salt is combined with the password before hashing.
- Even if two users have the same password, their hash values will be different when their salts are different.
- It helps protect against precomputed attacks such as rainbow table attacks.

## Procedure

1. Open VS Code.
2. Create a new Python file.
3. Import the required Python libraries.
4. Enter a sample password.
5. Generate a hash of the password without using a salt.
6. Generate a random salt.
7. Combine the password with the salt.
8. Generate a hash of the salted password.
9. Display both hash values.
10. Repeat the process with the same password and a new salt.
11. Compare the generated hash values.
12. Analyze how salting improves password security.

## Working of Password Hashing Without Salt

1. Enter a password.
2. Apply a hashing algorithm such as SHA-256.
3. Generate the hash value.
4. Store the hash instead of the original password.
5. Use the same password again and observe that the hash remains the same.

## Working of Password Hashing With Salt

1. Enter a password.
2. Generate a random salt.
3. Combine the password with the salt.
4. Apply the hashing algorithm.
5. Generate the salted hash.
6. Repeat with a new salt and observe that the hash value changes.

## Comparison Between Hashing With and Without Salt

| Feature | Without Salt | With Salt |
|---|---|---|
| Salt | Not used | Used |
| Same Password | Produces the same hash | Produces different hashes with different salts |
| Rainbow Table Attack | More vulnerable | Much harder |
| Security | Lower | Better |
| Implementation | Simple | Requires salt generation and storage |

## Resistance Against Password Attacks

- **Brute Force Attack:** Attackers try different password combinations until they find the correct one. Salting does not stop brute-force attacks, but using a slow password hashing algorithm makes them more difficult.
- **Dictionary Attack:** Attackers try commonly used passwords. Salting makes precomputed password hashes less useful.
- **Rainbow Table Attack:** Attackers use precomputed tables of password hashes. Unique salts help protect against these attacks.

## Result
Successfully implemented password hashing with and without salting using Python in VS Code. Compared both methods and observed that salting improves password security by making precomputed hash attacks more difficult.

## Conclusion
In this experiment, we learned how passwords can be stored using hashing techniques. We understood that hashing without salt is less secure because the same password always produces the same hash. Adding a unique random salt improves security and makes password attacks more difficult.

For real-world applications, password-specific hashing algorithms such as Argon2id, bcrypt, or scrypt are preferred over plain SHA-256.