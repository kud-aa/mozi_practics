# Cryptanalysis Affine Cipher

import argparse
import detectEnglish, cryptomath, affine_cipher

def main():
    parser=argparse.ArgumentParser(description="Cryptanalysis of Affine Cipher")
    parser.add_argument('-i','--input',
                        help="For input paste string or path for the file"
                        "",required=True)
    args = parser.parse_args()

    myMessage = args.input
    #myMessage = """U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG'<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""
    #myMessage = """V(t>I]]IhS]<r4_r<>_r*4<&hH<T*4h<]I>I)_H<]TSrI>TSr]<rh;<I?T_]<hiiTHT?<t|<hr4TH<}Th})T<RI))<tT<HT>h=T?z<HT~_H?)T]]<hi<R4Tr4TH<hH<Shr<r4h]T<I?T_]<4_=T<_}}T_HT?<hS<AT??IrE<m)_r_Sr<HT}h]rIS~<_S?<})_~I_HI]><>_|<HT]()r<IS<_<t_S"""
    #myMessage = """|J5-x1C#x185-m{.Ff5-mx_58-Q?-5x8b-?{-T1Q?5-F851)<1Q5t.fb-'{mmxt.)fQt5-Qt?51<x'580-|J5-#1{C1xm-.5<Qt58-TJx?-x1CFm5t?8-Q?-15*FQ158"-xt.-x1C#x185-TQff-<QCF15-{F?-J{T-?{-#x185-?J{85-{F?-{<-8b80x1CM0-|J5-x1C#x185-m{.Ff5-xf8{-xF?{mx?Q'xffb-C5t51x?58-J5f#-xt.-F8xC5-m588xC58-xt.-Q88F58-511{18-TJ5t-F8518-CQM5-?J5-#1{C1xm-QtMxfQ.-x1CFm5t?80Q"""
    #myMessage = "SI~~TH<SI~~TH<_>h~(]<?h<Shr"

    try:
        with open(args.input) as file:
            myMessage = file.read()
            hackedMessage = hackAffine(myMessage)
            with open('cry_aff.txt', 'w') as f:
                print(hackedMessage, file=f)
                print("Full encryption in cry_aff.txt")

    except:
        myMessage = args.input
        hackedMessage = hackAffine(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')

def hackAffine(message):

    # brute-force by looping through every possible key
    for key in range(95 ** 2):
        keyA = key // 95
        keyB = key % 95
        if cryptomath.egcd(keyA, 95)[0] != 1:
            continue

        key_arr = [keyA, keyB]
        decryptedText = affine_cipher.affine_decrypt(message, key_arr, 95, ' ')
        #print('Tried Key pair A: {:2d} B: {:2d} Text: {:20s}'.format(keyA, keyB, decryptedText[:20]))

        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.
            print('Possible encryption hack:')
            print('Key pair A: {} B: {}'.format(keyA, keyB))
            print('Decrypted message:')
            print (decryptedText[:200])
            print()

            return decryptedText
    return None

if __name__ == '__main__':
    main()
