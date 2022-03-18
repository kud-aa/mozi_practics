import random

alphabet = ''.join(chr(i) for i in range(65536))
plaintext = "Hey, this is really fun! AMOGUS ඞඞඞ"

def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    keyIndices = [alphabet.index(k) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def decrypt(cipher, key, alphabet):
    keyIndices = [key.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)

key = makeKey(alphabet)

cipher = encrypt(plaintext, key, alphabet)

print(plaintext)
print(cipher.encode('utf-8', 'replace').decode())
print(decrypt(cipher, key, alphabet))
