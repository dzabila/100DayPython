# Cesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# function encrypt
direction = input("Type 'encode' to encrypt, tpye 'decode' to decrypt\n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text, shift):
  encrypted_text = ""
  for letter in text:
    letter_index = alphabet.index(letter)
    if letter_index + shift > 25:
      letter_index = -1
      encrypted_text += alphabet[letter_index + shift]
    else:
      encrypted_text += alphabet[letter_index + shift]
  print(encrypted_text)
def decrypt(text, shift):
  decrypted_text = ""
  for letter in text:
    letter_index = alphabet.index(letter)
    if letter_index - shift < 0:
      letter_index = 26
      decrypted_text += alphabet[letter_index - shift]
    else:
      decrypted_text += alphabet[letter_index - shift]
  print(decrypted_text)

def caesar():
  if direction == "encode":
    encrypt(text, shift)

  elif direction == "decode":
    decrypt(text, shift)

  else:
    print("Invalid Input!!!")
caesar()
answer = input("Do you want another game? : Yes / No  :::  ").lower()

while answer != "no":
  direction = input("Type 'encode' to encrypt, tpye 'decode' to decrypt\n").lower()
  caesar()
  text = input("Type your message: \n").lower()
  shift = int(input("Type the shift number:\n"))
  answer = input("Do you want another game? : Yes / No  :::  ").lower()
