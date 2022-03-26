# Implementation of Affine Cipher in Python
# number of symbols in UTF-16 is 65536
# first symbol in unicode is \x00
# re - regular expression
import re
from cryptomath import egcd, modinv

# affine cipher encryption function 
# returns the cipher text
def affine_encrypt(text, key, power, first_symbol):

    '''

    C = (a*P + b) % power

    '''

    return ''.join([ chr((( key[0]*(ord(t) - ord(first_symbol)) + key[1] ) % power) 
                         + ord(first_symbol)) for t in text ])

# affine cipher decryption function 
# returns original text
def affine_decrypt(cipher, key, power, first_symbol):

    '''

    P = (a^-1 * (C - b)) % power

    '''

    return ''.join([ chr((( modinv(key[0], power)*(ord(c) - ord(first_symbol) - key[1])) 
                          % power) + ord(first_symbol)) for c in cipher ])


# Driver Code to test the above functions
def main():

    # declaring text and key
    #text = 'AFFINE CIPHER abcd !?! КИРИЛИЦА ريكرو $€£'
    #a, b = 17, 20

    menu = input("Choose text format [-f] for file or [-s] string ")
    if (menu == "s"):
        text = input("Type text: ")
    elif (menu == "f"):
        text = open("input.txt").read()
    else:
        print("Wrong option choose [-f] or [-s]")
        quit()

    a = int(input("Type A: "))
    b = int(input("Type B: "))

    key = [a, b]
    affine_encrypted_text = affine_encrypt((re.sub('[^a-zA-Z]+', '', text)).upper(), key, 26, 'A')

    # calling encryption function
    if (menu == "s"):
        print('Encrypted Text: {}'.format( affine_encrypted_text ))
    elif (menu == "f"):
        with open('enc_out.txt', 'w') as f:
            print(affine_encrypted_text, file=f)

    # calling decryption function
    if (menu == "s"):
        print('Decrypted Text: {}'.format
              ( affine_decrypt(affine_encrypted_text, key, 26, 'A') ))
    elif (menu == "f"):
        with open('dec_out.txt', 'w') as f:
            print(affine_decrypt(affine_encrypted_text, key, 26, 'A'), file=f)

if __name__ == '__main__':
    main()
