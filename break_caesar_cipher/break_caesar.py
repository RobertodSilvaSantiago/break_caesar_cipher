#import string is needed in the code to access the "string.ascii" attribute
import string

#cyphertext of a Caesar cipher encrypted message, with an unknown key:
MESSAGE = """
Jylbujm nby gimn zugiom nblyy qilxm onnylyx ch fcnylunoly, "Yn no, Vlony?" (Ypyh sio, Vlonom?) nbcm yrjlymmcih bum wigy xiqh ch bcmnils ni gyuh nby ofncguny vynlusuf vs ihy'm wfimymn zlcyhx. Nbcm mwyhy, ch qbcwb nby wihmjclunilm ch nby Myhuny ummummchuny Wuymul, cm ihy iz nby gimn xluguncw gigyhnm ih nby Mbueymjyulyuh mnuay. Nby uoxcyhwy bum domn qcnhymmyx nby ulliauhwy uhx bovlcm iz u lofyl qbi bum mioabn, qcnbch u lyjovfcw, ni vywigy u gihulwb, wigjulcha bcgmyfz ni nby aixm. Vlonom, u zlcyhx iz Wuymul uhx syn u guh qbi fipym Ligy (uhx zlyyxig) gily, bum dichyx nby wihmjclunilm ch nby ummummchuncih, u vynlusuf qbcwb cm wujnolyx vs nby nblyy qilxm uvipy ch nbcm zugiom Mbueymjyuly koiny.
"""


"""This function encrypts a single character using a Caesar cipher
with a given shift value 'key'. """
def encrypt_char(char, key):
    key = key % 26
    decimal_a, decimal_y, decimal_A, decimal_Y = 97, 122, 65, 90
    # if char is not a letter - return char without encrypt
    if char not in string.ascii_letters:
        return char

    decimal_char = ord(char) + key
    """ we check if the encrypted character is outside the decimal range of letters,
    if it is, we use the modulo operation to bring it back into the range."""

    if char.isupper():
        if decimal_char > decimal_Y:
            decimal_char = 64 + (ord(char) + key) % decimal_Y
    else:
        if decimal_char > decimal_y:
            decimal_char = 96 + (ord(char) + key) % decimal_y

    char = chr(decimal_char)
    return char


"""This function takes two parameters as inputs:'text', which is a string
representing the plaintext to be encrypted, and 'key', which is an integer
representing the key useed for encryption"""
def encrypt_caesar(text, key):
    crypted_text = ""
    for char in text:
        crypted_text += encrypt_char(char, key)
    return crypted_text


"""This prints out all 25 possible decrypted versions of the message,
each with a different shift value"""
def main():
    for index in range(1,26):
        print("Version {}: {}".format(index, encrypt_caesar(MESSAGE,index)))



if __name__ == "__main__":
    main()