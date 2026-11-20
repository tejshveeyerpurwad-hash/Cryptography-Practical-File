import hashlib
def hash(msg):
    sha = hashlib.sha256()
    sha.update(msg.encode('utf-8'))
    return sha.hexdigest()
Original = input("Enter the Original Message: ")
originalHash = hash(Original)
received = input("Enter the message for verification: ")
receivedHash = hash(received)
print("Original Hash:", originalHash)
print("Received Hash:", receivedHash)
if originalHash == receivedHash:
    print("Verification successful! The messages match.")
else:
    print("Verification failed! The messages do not match.")