import hashlib
import random

def insecure_crypto_prng():
    # Insecure use of random module for generating cryptographic keys
    random_key = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
    
    # Print the generated key (omitted for brevity)
    print(random_key)

if __name__ == "__main__":
    insecure_crypto_prng()
