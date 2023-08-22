def main():
    plain_text=input("enter plain text:")
    key=int(input("enter key:"))
    plain_text=plain_text.upper
    cipher_arr=[]
    for i in range(len(plain_text)):

        char=plain_text[i]
        cipher_char=chr((ord(char)-65+key% 26)+65)
        cipher_arr.append(cipher_char)
    print(cipher_arr)


main()