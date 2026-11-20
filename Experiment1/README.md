# Experiment 1: Implementation of Caesar, Vigenère, and Rail Fence Ciphers

## Aim
To implement Caesar, Vigenère, and Rail Fence ciphers using CrypTool and understand how encryption and decryption work in each method.

## Software Used
- CrypTool

## Introduction
Encryption is a process of converting a normal readable message (plaintext) into a secret message (ciphertext) so that unauthorized people cannot easily understand it.

In this experiment, we use three traditional encryption techniques:

### 1. Caesar Cipher
Caesar Cipher is a simple substitution technique. Each letter in the message is shifted by a fixed number of positions in the alphabet.

For example, if the key is 3:
- A becomes D
- B becomes E
- C becomes F

During decryption, the letters are shifted backward by the same number.

### 2. Vigenère Cipher
Vigenère Cipher is a substitution technique that uses a keyword to encrypt the message. Each letter is shifted according to the corresponding letter of the key.

The same keyword is used during decryption to recover the original message.

### 3. Rail Fence Cipher
Rail Fence Cipher is a transposition technique. It rearranges the letters of the original message in a zigzag pattern across multiple rows (rails).

During decryption, the letters are placed back in their original positions to recover the message.

## Procedure
1. Open CrypTool software.
2. Enter a plaintext message for encryption.
3. Select the Caesar Cipher and enter the required key.
4. Encrypt the message and observe the ciphertext.
5. Decrypt the ciphertext using the same key.
6. Repeat the same process using the Vigenère Cipher with a keyword.
7. Select the Rail Fence Cipher and enter the required number of rails.
8. Encrypt and decrypt the message.
9. Compare the encryption and decryption results of all three techniques.

## Comparison

| Cipher | Technique | Key Used |
|---|---|---|
| Caesar Cipher | Substitution | Number |
| Vigenère Cipher | Substitution | Keyword |
| Rail Fence Cipher | Transposition | Number of Rails |

## Result
Successfully implemented Caesar, Vigenère, and Rail Fence ciphers using CrypTool. Observed their encryption and decryption processes and understood the differences between these three techniques.

## Conclusion
In this experiment, we learned how different classical encryption techniques work. Caesar and Vigenère ciphers replace letters, while the Rail Fence cipher changes the positions of letters. We also learned how the original message can be recovered through decryption using the correct key.