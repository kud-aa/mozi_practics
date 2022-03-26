import random
import re

alphabet = ''.join(chr(i) for i in range(65,91))

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

    menu = input("Choose text format [-f] for file or [-s] string ")
    if (menu == "s"):
        text = input("Type text: ")
    elif (menu == "f"):
        text = open("input.txt").read()
    else:
        print("Wrong option choose [-f] or [-s]")
        quit()

    key = makeKey(alphabet)
    print(key)
    #text = 'AFFINE RECURSIVE CIPHER abcd !?! KИРИЛЛИЦА ريكرو $€£'

    cipher = encrypt((re.sub('[^a-zA-Z]+', '', text)).upper(), key, alphabet)

    if (menu == "s"):
        print("Ciphertext: {}".format(cipher.encode('utf-8', 'replace').decode()))
    elif (menu == "f"):
        with open('enc_out.txt', 'w') as f:
            print(cipher.encode('utf-8', 'replace').decode(), file=f)

    if (menu == "s"):
        print("Расшифрованный текст: {}".format(decrypt(cipher, key, alphabet)))
    elif (menu == "f"):
        with open('dec_out.txt', 'w') as f:
            print(decrypt(cipher, key, alphabet), file=f)

if __name__ == '__main__':
    main()
