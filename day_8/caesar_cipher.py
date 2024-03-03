import alphabet
import logo

print(logo.ascii_logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Input your message here : ").lower()
shift = int(input("Input your shift here: "))


def caesar(direct=direction, txt=text, sft=shift):
    if direct == "encode" or direct == "decode":
        if isinstance(sft, int):
            final_text = ""
            if direct == "decode":
                sft *= -1
            for letter in txt:
                if letter.isalpha():
                    first_position = alphabet.list_alphabet.index(letter)
                    position = (first_position + sft) % len(alphabet.list_alphabet)
                    final_text += alphabet.list_alphabet[position]
                else:
                    final_text += letter
            print(f"The {direct}d text is {final_text}")
        else:
            print("You input the wrong shift")
    else:
        print(f"You input the wrong direction")


caesar(direction, text, shift)
