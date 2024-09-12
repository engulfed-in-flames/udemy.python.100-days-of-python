# Caesar Cipher: https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
# a to z => 97 to 122

import art

# fmt: off
def caesar(original_text, shift, encode_or_decode):
    output = ""

    if encode_or_decode == "decode":
        shift *= -1

    for char in original_text:
        shifted_index = None

        if char not in alphabets:
            output += char
        else:
            shifted_index = alphabets.index(char) + shift
            shifted_index %= len(alphabets)

            output += alphabets[shifted_index]

    return output

def should_continue():
    while True:
        answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if answer == "yes":
            return True
        elif answer == "no":
            return False

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
restart = True

print(art.logo)

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypted = caesar(message, shift, "encode")
        print(f"Here's the encoded result: {encrypted}")
    elif direction == "decode":
        decrypted = caesar(message, shift, "decode")
        print(f"Here's the decoded result: {decrypted}")
    else:
        print("The action is NOT allowed.")

    restart = should_continue()
