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
 
def recursive_encrypt(text, alpha, beta):

    out = []
    for t in text:
        i = text.index(t)
        if (i > 1):
            alpha[2] = (alpha[0] * alpha[1]) % 65536
            beta[2] = (beta[0] + beta[1]) % 65536
        else:
            if (i == 0):
                alpha[2] = alpha[0]
                beta[2] = beta[0]
            else:
                alpha[2] = alpha[1]
                beta[2] = beta[1]

        alpha[0] = alpha[1]
        alpha[1] = alpha[2]
        beta[0] = beta[1]
        beta[1] = beta[2]

        out.append(chr((alpha[2]*ord(t) + beta[2]) % 65536))
    return "".join(out)

def recursive_decrypt (cipher, alpha, beta):

    out = []
    for c in cipher:
        i = cipher.index(c)
        if (i > 1):
            alpha[2] = (alpha[0] * alpha[1]) % 65536
            beta[2] = (beta[0] + beta[1]) % 65536
        else:
            if (i == 0):
                alpha[2] = alpha[0]
                beta[2] = beta[0]
            else:
                alpha[2] = alpha[1]
                beta[2] = beta[1]

        alpha[0] = alpha[1]
        alpha[1] = alpha[2]
        beta[0] = beta[1]
        beta[1] = beta[2]

        out.append(chr(( modinv(alpha[2], 65536)*(ord(c) - beta[2])) % 65536))

    return "".join(out)

# Driver Code to test the above functions

def main():

    # declaring text and key

    #text = input("Введите текст: ")
    #a = int(input("введите a: "))
    #b = int(input("Введите b: "))
    text = 'AFFINE CIPHER abcd !?! КИРИЛИЦА ريكرو $€£'
    alpha = [7, 3, None]
    beta = [10, 8, None]

    # calling recursive encryption function
    recursive_encrypted_text = recursive_encrypt(text, alpha, beta)
    print('Recursive encrypted text: {}'.format( recursive_encrypted_text ))
    #print('Recursive decrypted Text: {}'.format
    #      ( recursive_decrypt(recursive_encrypted_text, alpha, beta) ))

if __name__ == '__main__':

    main()
