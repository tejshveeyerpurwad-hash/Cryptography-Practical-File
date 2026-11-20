
p = int(input("Enter a prime number p: "))
g = int(input("Enter the Generator g: "))

a = int(input("Enter Alice's private key a: "))
b = int(input("Enter Bob's private key b: "))

print(f"p: {p}, g: {g}, a: {a}, b: {b}")

A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's Public Key:", A)
print("Bob's Public Key:", B)

s1 = pow(B, a, p)
s2 = pow(A, b, p)

print("Shared Secret Key for Alice:", s1)
print("Shared Secret Key for Bob:", s2)

if s1 == s2:
    print("Shared Secret Key is same for both Alice and Bob")
else:
    print("Shared Secret Key is different for Alice and Bob")
