# Implementation of Affine Cipher in Python

# Extended Euclidean Algorithm for finding modular inverse
# eg: modinv(7, 65536) = 15
# number of symbols in UTF-16 is 65536
# first symbol is \x00
def egcd(a, b):

    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b

    return gcd, x, y

def modinv(a, m):

    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


# affine cipher encryption function 
# returns the cipher text
def affine_encrypt(text, key):

    '''

    C = (a*P + b) % 65536

    '''

    return ''.join([ chr((( key[0]*(ord(t) - ord('\x00')) + key[1] ) % 65536) 
                         + ord('\x00')) for t in text ])


# affine cipher decryption function 
# returns original text
def affine_decrypt(cipher, key):

    '''

    P = (a^-1 * (C - b)) % 65536

    '''

    return ''.join([ chr((( modinv(key[0], 65536)*(ord(c) - ord('\x00') - key[1])) 
                          % 65536) + ord('\x00')) for c in cipher ])


# Driver Code to test the above functions
def main():

    # declaring text and key
    text = 'AFFINE CIPHER abcd !?! КИРИЛИЦА ريكرو $€£'
    a, b = 17, 20

    #text = input("Введите текст: ")
    #a = int(input("введите a: "))
    #b = int(input("Введите b: "))
    key = [a, b]


    # calling encryption function
    affine_encrypted_text = affine_encrypt(text, key)
    print('Encrypted Text: {}'.format( affine_encrypted_text ))

    # calling decryption function
    print('Decrypted Text: {}'.format
          ( affine_decrypt(affine_encrypted_text, key) ))

if __name__ == '__main__':
    main()
