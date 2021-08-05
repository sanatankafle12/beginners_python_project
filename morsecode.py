morse_code_dictionary = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

key_list = list(morse_code_dictionary.keys())
val_list = list(morse_code_dictionary.values())


def decrypt():
    while True:
        decrypted = []
        list_to_decrypt = list(map(str,input("Encrpyt coode to decrypt use '\\' for seperating words:\n").strip().split()))
        for i in list_to_decrypt:
            if i in  val_list or i == "\\":
                if i =="\\":
                    decrypted.append(" ")
                else:
                    position = val_list.index(i)
                    decrypted.append(key_list[position])
            else:
                print("Invalid.. ")
                
        print("".join(decrypted))   
        break



def encrypt():
    while True:
        encrypted = []
        string = input("Encrpyt code to encrypt :\n").upper()
        list_to_encrypt = []
        for i in string:
                list_to_encrypt.append(i)
        for i in list_to_encrypt:
            if i in key_list or i == " ":
                if i == " ":
                    encrypted.append("\\")
                else:
                    encrypted.append(morse_code_dictionary[i])
            else:
                print("Invalid..")
        print("NOTE: \\ represents seperation of words and space represents seperation of letters.\n\n" )
        print("  ".join(encrypted))
        break



if __name__ == "__main__":
    while True:
        n = input("USe e to encrpyt and d to decrypt and q to quit::\n")
        if n=='e':
            encrypt()
        elif n=='d':
            decrypt()
        elif n=='q':
            print("BYE BYE!!")
            break
        else:
            print("Invalid.. \n")