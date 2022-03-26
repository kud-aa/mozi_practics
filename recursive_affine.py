# Implementation of Recursive Affine Cipher in Python
# number of symbols in UTF-16 is 65536
# first symbol in unicode is \x00

from cryptomath import egcd, modinv

# recursive affine cipher encryption function 
# returns the cipher text
def recursive_encrypt(text, alpha1, alpha2, beta1, beta2, power, first_symbol):

    '''

    y_i = (a_i*x_i + b_i) % power

    '''

    out = ''
    for t in text:
        out += chr((( alpha1*(ord(t) - ord(first_symbol)) + beta1 ) % power) + ord(first_symbol))
        alpha1, alpha2 = alpha2, (alpha1 * alpha2) % power
        beta1, beta2 = beta2, (beta1 + beta2) % power
    return out

# recursive affine cipher decryption function 
# returns original text
def recursive_decrypt(cipher, alpha1, alpha2, beta1, beta2, power, first_symbol):

    '''

    x_i = ((a_i)^-1*(y_i - b_i)) % power

    '''

    out = ''
    for c in cipher:
        out += chr((( modinv(alpha1, power)*(ord(c) - ord(first_symbol) - beta1 )) % power) + ord(first_symbol))
        alpha1, alpha2 = alpha2, (alpha1 * alpha2) % power
        beta1, beta2 = beta2, (beta1 + beta2) % power
    return out

# Driver Code to test the above functions
def main():

    # declaring text and alphas & betas
    text = 'AFFINE RECURSIVE CIPHER abcd !?! KИРИЛЛИЦА ريكرو $€£'
    alpha1 = 7
    alpha2 = 11
    beta1  = 10
    beta2  = 13

    #text = input("Введите текст: ")
    #alpha1 = int(input("Введите alpha1: "))
    #alpha2 = int(input("Введите alpha2: "))
    #beta1  = int(input("Введите beta1 : "))
    #beta2  = int(input("Введите beta2 : "))

    # calling recursive encryption function
    recursive_encrypted_text = recursive_encrypt(text, alpha1, alpha2, beta1, beta2, 65536, '\x00').encode('utf-8', 'replace').decode()
    print('Recursive encrypted text: {}'.format( recursive_encrypted_text ))

    ## calling recursive decryption function
    print('Recursive decrypted Text: {}'.format
          ( recursive_decrypt(recursive_encrypted_text, alpha1, alpha2, beta1, beta2, 65536, '\x00')))

if __name__ == '__main__':
    main()
