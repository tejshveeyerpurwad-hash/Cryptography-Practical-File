
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))

n = p * q
print("n =", n)

totient = (p - 1) * (q - 1)
print("Totient =", totient)

e = int(input("Enter a value for e (1 < e < totient and gcd(e, totient) = 1): "))
print("e =", e)

d = pow(e, -1, totient)
print("d =", d)

public_key = (e, n)
private_key = (d, n)

print("Public Key =", public_key)
print("Private Key =", private_key)

def encrypt(message, public_key):
    ciphertext = []
    for char in message:
        value = ord(char)
        encrypted = pow(value, public_key[0], public_key[1])
        ciphertext.append(encrypted)
    return ciphertext

def decrypt(ciphertext, private_key):
    decrypted_message = ""
    for value in ciphertext:
        decrypted_value = pow(value, private_key[0], private_key[1])
        decrypted_message += chr(decrypted_value)
    return decrypted_message

message = input("Enter a message to encrypt: ")

ciphertext = encrypt(message, public_key)
print("Ciphertext =", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted Message =", decrypted_message)
