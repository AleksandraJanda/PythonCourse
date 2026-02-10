alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    original_text.lower()
    shifted_text = ''
    for letter in original_text:
        shifted_id = alphabet.index(letter) + shift_amount
        if shifted_id >= len(alphabet):
            shifted_id = shifted_id-len(alphabet)
        shifted_text += alphabet[shifted_id]
    print(f'Encoded result: {shifted_text}')

def decrypt(original_text, shift_amount):
    original_text.lower()
    shifted_text = ''
    for letter in original_text:
        shifted_id = alphabet.index(letter) - shift_amount
        if shifted_id < 0:
            shifted_id = 0+shifted_id
        shifted_text += alphabet[shifted_id]
    print(f'Decoded result: {shifted_text}')

if direction == 'encode':
    encrypt(text,shift)
elif direction == 'decode':
    decrypt(text,shift)