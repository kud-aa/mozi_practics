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
 
def recursive_encrypt(text, alpha1, alpha2, beta1, beta2):
    out = ''
    for t in text:
        out += chr((( alpha1*(ord(t) - ord('\x00')) + beta1 ) % 65536) + ord('\x00'))
        alpha1, alpha2 = alpha2, (alpha1 * alpha2) % 65536
        beta1, beta2 = beta2, (beta1 + beta2) % 65536
    return out

def recursive_decrypt (cipher, alpha1, alpha2, beta1, beta2):
    out = ''
    for c in cipher:
        out += chr((( modinv(alpha1, 65536)*(ord(c) - ord('\x00') - beta1 )) % 65536) + ord('\x00'))
        alpha1, alpha2 = alpha2, (alpha1 * alpha2) % 65536
        beta1, beta2 = beta2, (beta1 + beta2) % 65536
    return out

# Driver Code to test the above functions
def main():

    # declaring text and key

    #text = input("Введите текст: ")
    #a = int(input("введите a: "))
    #b = int(input("Введите b: "))
    text = 'AFFINE CIPHER abcd !?! KИРИЛЛИЦА ريكرو $€£'
    #text = 'КИРИЛИЦА ريكرو $€£'
    alpha1 = 7
    alpha2 = 3
    beta1 = 10
    beta2 = 8

    # calling recursive encryption function
    recursive_encrypted_text = recursive_encrypt(text, alpha1, alpha2, beta1, beta2).encode('utf-8', 'replace').decode()
    print('Recursive encrypted text: {}'.format( recursive_encrypted_text ))
    print('Recursive decrypted Text: {}'.format
          ( recursive_decrypt(recursive_encrypted_text, alpha1, alpha2, beta1, beta2)))

if __name__ == '__main__':

    main()
