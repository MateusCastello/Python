from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run = True

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def ceasar (text, shift,direction):

  end_message = ""

  if direction == "encode":
    for letter in text:
      normal_index = alphabet.index(letter)
      end_message+=alphabet[(normal_index+shift)%26]
    print(f"The encoded message is: {end_message} \n")

  elif direction == "decode":
    shift_alphabet = []    
    for letter in range(26):    
      shift_alphabet.append(alphabet[(letter+shift)%26])

    for letter in text:    
      end_message+=alphabet[shift_alphabet.index(letter)]

    print(f"The decoded message is {end_message}")


def start():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceasar(text,shift, direction)



while run:
  start()
  opt = input("Do you wanna go again?").lower()
  if opt == "no":
    run = False
  elif opt == "yes":
    continue
  else:
    print("Not a valid option")
    run = False

  




