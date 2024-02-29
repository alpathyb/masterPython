import alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Input your shift number: "))


def encrypt(txt, sft):
    list_encrypt = []
    for i in txt:
        temp_index = alphabet.list_alphabet.index(i)
        temp_index += sft
        list_encrypt.append(alphabet.list_alphabet[temp_index])
    chipher_text = "".join(list_encrypt)
    print(f"The encode text is {chipher_text}")


encrypt(text, shift)
