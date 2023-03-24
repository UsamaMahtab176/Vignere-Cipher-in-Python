letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


def generateKey(text, keyword):
    keyword = list(keyword)
    if len(keyword) >= len(text):
        return "".join(keyword)
    if len(keyword) < len(text):
        for i in range(len(text) - len(keyword)):
            keyword.append(keyword[i % len(keyword)])
    return "".join(keyword)


def generateCipherText(text, key):
    cipherText = []
    text = list(text)
    key = list(key)
    for i in range(len(text)):
        x = letters[((ord(text[i]) + ord(key[i])) % 26)]
        cipherText.append(x)
    return "".join(cipherText)


def generateOriginalText(text, key):
    originalText = []
    text = list(text)
    key = list(key)
    for i in range(len(text)):
        x = letters[((ord(text[i]) - ord(key[i])) % 26)]
        originalText.append(x)
    return "".join(originalText)


choice = input(
    'Please choose your option  \n 1. Press 1 for ENCRYPTION of Text \n 2. Press 2 for DECRYPTION of Text \n')

if int(choice) == 1:

    keyword = input("Enter the Cipher Key!!! \n")
    text = input('Enter text you want to be encrycpted \n')
    text = text.upper()
    key = generateKey(text, keyword)
    key = key.upper()
    cipherText = generateCipherText(text, key)
    print("CipherText of given Original text by VigneresCipher is: \n" + cipherText)

elif int(choice) == 2:
    keyword = input("Enter the Cipher Key!!! \n")
    text = input('Enter text you want to be decrycpted \n')
    text = text.upper()
    key = generateKey(text, keyword)
    key = key.upper()
    originalText = generateOriginalText(text, key)
    print("Original Text of given CipherText by Vigeneres Cipher is: \n" + originalText)

else:
    print("Invalid Input!!!!")
