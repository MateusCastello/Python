from art import logo
print(logo)
alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run = True


def ceasar(text, shift, direction):
  
    end_message = ""

    if direction == "encode":
        for letter in text:
          if letter in alphabet:
            normal_index = alphabet.index(letter)
            end_message += alphabet[(normal_index+shift) % 26]
          else:
            end_message += letter
        print(f"The encoded message is:{end_message} \n")

    elif direction == "decode":
        shift_alphabet = []
        for letter in range(26):
            shift_alphabet.append(alphabet[(letter+shift) % 26])

        for letter in text:
            if letter in alphabet:
              end_message += alphabet[shift_alphabet.index(letter)]
            else:
              end_message += letter

        print(f"The decoded message is:{end_message}")

    else:
        print("Invalid option!")


def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)


while run:
    start()
    opt = input("Do you wanna go again? (yes or no) ").lower()
    if opt == "no":
        run = False
    elif opt == "yes":
        continue
    else:
        print("Not a valid option")
        run = False