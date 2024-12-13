from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def ceaser(plain_text,shift,direction):
      if direction =="decode":
        shift*=-1
      end_text=""
      for i in plain_text:
        if i in alphabet:
          position=alphabet.index(i)
          new_position=position+shift
          end_text+=alphabet[new_position]
        else:
          end_text+=i
      print(end_text)

stop = False
while not stop:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  ceaser(plain_text=text,shift=shift,direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    stop = True
    print("Goodbye")


