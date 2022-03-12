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
    for i in range(len(text)):
        if (i > 1):
            alpha[2] = (alpha[0] * alpha[1]) % 65536
            beta[2] = (beta[0] + beta[1]) % 65536
        else:
            alpha[2] = alpha[1]
            beta[2] = beta[1]

        alpha[0] = alpha[1]
        alpha[1] = alpha[2]
        beta[0] = beta[1]
        beta[1] = beta[2]

        #print("T: {0} | Symbol: {1:^3} | A: {2:5d} | B = {3:5d} | i = {4}".format(text[i], (chr((alpha[2]*ord(text[i]) + beta[2]) % 65536)), alpha[2], beta[2], i))
        out.append(chr(((alpha[2]*(ord(text[i]) - ord('\x00')) + beta[2])
                        % 65536) + ord('\x00')))
    return "".join(out)

    #return ''.join([ chr((( key[0]*(ord(t) - ord('\x00')) + key[1] ) % 65536) 
    #                     + ord('\x00')) for t in text ])

def recursive_decrypt (cipher, alpha, beta):

    out = []
    for i in range(len(cipher)):
        if (i > 1):
            alpha[2] = (alpha[0] * alpha[1]) % 65536
            beta[2] = (beta[0] + beta[1]) % 65536
        else:
            alpha[2] = alpha[1]
            beta[2] = beta[1]

        alpha[0] = alpha[1]
        alpha[1] = alpha[2]
        beta[0] = beta[1]
        beta[1] = beta[2]

        out.append(chr((( modinv(alpha[2], 65536)*(ord(cipher[i]) - ord('\x00') - beta[2]))
                        % 65536) + ord('\x00')))

    return "".join(out)
    #return ''.join([ chr((( modinv(key[0], 65536)*(ord(c) - ord('\x00') - key[1])) 
    #                      % 65536) + ord('\x00')) for c in cipher ])

# Driver Code to test the above functions

def main():

    # declaring text and key

    #text = input("Введите текст: ")
    #a = int(input("введите a: "))
    #b = int(input("Введите b: "))
    text = 'AFFINE CIPHER abcd !?! ИРИЛИЦА ريكرو $€£'
    #text = 'КИРИЛИЦА ريكرو $€£'
    alpha = [7, 3, None]
    beta = [10, 8, None]
    alpha1 = [7, 3, None]
    beta1 = [10, 8, None]

    # calling recursive encryption function
    recursive_encrypted_text = recursive_encrypt(text, alpha, beta)
    print('Recursive encrypted text: {}'.format( recursive_encrypted_text ))
    print('Recursive decrypted Text: {}'.format
          ( recursive_decrypt(recursive_encrypted_text, alpha1, beta1) ))

if __name__ == '__main__':

    main()
