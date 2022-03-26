import random

#alphabet = ''.join(chr(i) for i in range(65,91))
alphabet = ''.join(chr(i) for i in range(65536))

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

def main():
    key = makeKey(alphabet)
    #print(key)

    #plaintext = 'AFFINE RECURSIVE CIPHER abcd !?! KИРИЛЛИЦА ريكرو $€£'
    plaintext = input("Введите текст: ")

    cipher = encrypt(plaintext, key, alphabet)

    print("Шифртекст: {}".format(cipher.encode('utf-8', 'replace').decode()))
    print("Расшифрованный текст: {}".format(decrypt(cipher, key, alphabet)))

if __name__ == '__main__':
    main()
