# Experiment 2: Frequency Analysis on Classical Ciphers

## Aim
To perform frequency analysis on classical ciphers and understand how easily they can be broken using letter frequency patterns.

## Software Used
- CrypTool

## Introduction
Frequency analysis is a way to break encrypted messages by looking at how often letters appear in the ciphertext.

In English, some letters like E, T, A, O, and I appear more often than others. By comparing letter frequencies in the encrypted text with normal English letter frequencies, we can try to figure out the original message.

This technique is mainly useful for analyzing classical substitution ciphers, such as the Caesar Cipher.

## Procedure
1. Open CrypTool software.
2. Enter a plaintext message.
3. Encrypt the message using a classical cipher, such as the Caesar Cipher.
4. Observe the encrypted message (ciphertext).
5. Open the frequency analysis tool in CrypTool.
6. Analyze how frequently each letter appears in the ciphertext.
7. Compare the frequency of letters with normal English letter frequencies.
8. Try to identify the original letters using the frequency patterns.
9. Check whether the original message can be recovered.
10. Observe how frequency analysis helps in breaking classical encryption techniques.

## Working of Frequency Analysis
- First, the encrypted message is collected.
- The number of occurrences of each letter is counted.
- The most frequently occurring letters are identified.
- These letters are compared with common English letters.
- Based on the comparison, possible original letters are identified.
- The guessed message is checked to see whether it makes sense.

## Analysis
Frequency analysis is effective against simple substitution ciphers because they preserve the frequency pattern of letters.

For example:
- Caesar Cipher can be broken easily using frequency analysis.
- Simple substitution ciphers can also be analyzed using letter patterns.
- Vigenère Cipher is more difficult to analyze because it uses multiple substitution patterns, but it can still be vulnerable to frequency-based attacks under certain conditions.

## Result
Performed frequency analysis using CrypTool and studied how often letters appear in encrypted text. Observed how frequency patterns can help identify the original message.

## Conclusion
In this experiment, we learned how frequency analysis works and how it can be used to analyze classical encryption techniques. We understood that simple substitution ciphers are weak against frequency analysis because they keep the original letter frequency patterns.