# Implementation of Substitution Cipher in Python

import argparse
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

    parser=argparse.ArgumentParser(description="Substitution Cipher")
    parser.add_argument('-i','--input',
                        help="For input paste string or path for the file"
                        "",required=True)
    args = parser.parse_args()

    key = makeKey(alphabet)
    print("Used key: {}".format(key))

    try:
        with open(args.input) as file:
            text = file.read()
            cipher = encrypt((re.sub('[^a-zA-Z]+', '', text)).upper(), key, alphabet)
            with open('sub_enc_out.txt', 'w') as f:
                print(cipher.encode('utf-8', 'replace').decode(), file=f)
                print("Encrypted text in sub_enc_out.txt file")
            with open('sub_dec_out.txt', 'w') as f:
                print(decrypt(cipher, key, alphabet), file=f)
                print("Decrypted ciphertext in sub_dec_out.txt file")
    except:
        text = args.input
        cipher = encrypt((re.sub('[^a-zA-Z]+', '', text)).upper(), key, alphabet)
        print("Encrypted text: {}".format(cipher.encode('utf-8', 'replace').decode()))
        print("Decrypted ciphertext: {}".format(decrypt(cipher, key, alphabet)))

if __name__ == '__main__':
    main()
