import random
import time
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m
 # key generation for rsa
def generate_keys():
    p = 61
    q = 53
    n = p * q
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = modinv(e, phi)
    return (e, n), (d, n)
 # encrypt plaintext using caesar cipher
def encrypt_caesar(plaintext, shift):
    ct = ""

    for char in plaintext:
        if (char.isupper()):
            ct += chr((ord(char) + shift-65) % 26 + 65)
        else:
            ct += chr((ord(char) + shift - 97) % 26 + 97)

    return ct
 # decrypt text of rsa using caesar cipher to obtained plaintext
def decrypt_caesar(ciphertext, shift):
    pt = ""

    for char in ciphertext:
        if (char.isupper()):
            pt += chr((ord(char) - shift-65) % 26 + 65)
        else:
            pt += chr((ord(char) - shift - 97) % 26 + 97)
 
    return pt
  # encrypt ciphertext of caesar cipher using rsa
def encrypt_rsa(plaintext, pu):
    e, n = pu
    lst = []
    for char in plaintext:
        m = ord(char)
        c = pow(m, e) % n
        lst.append(str(c))
   
    ct = " ".join(lst)
    return ct
  # decrypt the ciphertext using rsa
def decrypt_rsa(ciphertext, pr):
    d, n = pr
    lst = ciphertext.split(' ')
    pt = ''
    for char in lst:
        c = int(char)
        m = pow(c, d) % n
        pt += chr(m)
    return pt

if __name__ == "__main__":
    plaintext = ""
    file = open('C:/Users/intel/Desktop/file.txt', 'r')
    while 1:  
        # read by character
        char = file.read(1)        
        if not char:
            break  
        plaintext+=char         #Taking data from the file
    file.close()
    shift = random.randint(0,len(plaintext))
    start=time.time()
    ciphertext1 = encrypt_caesar(plaintext, shift)
    print("CAESAR ENCRYPTED TEXT:",ciphertext1)
    print()
    pu, pr = generate_keys()
    ciphertext2 = encrypt_rsa(ciphertext1, pu)
    print("RSA ENCRYPTED TEXT:",ciphertext2)
    print()
    # encryption time
    end=time.time()
    print("TOTAL ENCRYPTION TIME:",end-start)

    start=time.time()
    plaintext1 = decrypt_rsa(ciphertext2, pr)
    print("RSA DECRYPTED TEXT:",plaintext1)
    print()
    plaintext2 = decrypt_caesar(plaintext1, shift)
    print("CAESAR DECRYPTED TEXT:",plaintext2)
    end=time.time()
    # decryption time
    print("TOTAL DECRYPTION TIME:",end-start)
