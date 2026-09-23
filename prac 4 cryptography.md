# Practical 4: Cryptography

## Aim 

To study different cryptographic techniques such as encryption, hashing and digital signatures, and implement them using a real-world application.

## Requirements 

- Computer/laptop
- Python 3.x
- VS Code / Google Colab / Juypter Notebook
- Python Cryptography Library

## Introduction

Cryptography is the technique of protecting information by converting it into a form that prevents unauthorized access or modification.

The major techniques used are: 
- **Encryption**: Converts plaintext into ciphertext to protect confidentiality.
- **Hashing**: Converts data into a fixed-length hash value to verify data integrity.
- **Digital Signature**: Uses cryptography to verify the authenticity and integrity of a message or document.

## Procedure

1. Install the required Python cryptography library.
2. Create a sample message representing sensitive information.
3. Encrypt the message using a symmetric encryption algorithm.
4. Decrypt the ciphertext to retrieve the original message.
5. Generate a hash of the message using a hashing algorithm.
6. Modify the message and generate its hash again to demonstrate integrity verification.
7. Generate a digital key pair.
8. Create a digital signature for the message using the private key.
9. Verify the signature using the corresponding public key.
10. Observe and record the results.

## Implementation

### **A. Encryption and Decryption**

```
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Confidential Data"

encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
```

Result: The original message is converted into ciphertext and can be recovered using the correct key.

### **B. Hashing**

```
import hashlib

message = "Confidential Data"

hash_value = hashlib.sha256(message.encode()).hexdigest()

print("SHA-256 Hash:", hash_value)
```

Result: A fixed-length SHA-256 hash is generated for the message.

### **C. Digital Signature**

```
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

message = b"Verified Document"

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Digital Signature: Valid")
```

Result: The digital signature is successfully verified, confirming the authenticity and integrity of the message.

## Applications

| Technique               | Real-World Application                          |
| ----------------------- | ----------------------------------------------- |
| Encryption              | Secure messaging, online banking, HTTPS         |
| Hashing                 | Password storage, file integrity verification   |
| Digital Signatures      | E-documents, software signing, online contracts |
| Symmetric Encryption    | Secure storage and communication                |
| Asymmetric Cryptography | Secure key exchange and authentication          |


## Results

Encryption, hashing and digital signatures were successfully studied and implemented using Python. Encryption provided confidentiality, hashing provided integrity verification, and digital signatures provided authentication and integrity.

## Conclusion

Cryptographic techniques are essential for securing modern digital systems. Encryption protects information from unauthorized access, hashing detects changes to data, and digital signatures verify the authenticity and integrity of digital information.
