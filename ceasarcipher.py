alphabet = ['a','b', 'c', 'd','e','f','g','h','i','j', 'k','l', 'm','n','o','p',
            'q','r','s','t','u','v','w','x','y','z','a','b', 'c', 'd','e','f',
            'g','h','i','j', 'k','l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = (input("Type ' encode' to encrypt, type'decode'to dycrpt:\n "))
text =input("Type your message:\n").lower()
shift =int(input("Type the shift number:\n"))

shift = shift % 26

#simplest way


def ceasar(start_text, shift_amount, cipher_direction):
    end_text = "" 
    if cipher_direction == "decode": 
        shift_amount *= -1
    for char in start_text: 
       if char in alphabet:           
          position = alphabet.index(char) 
          new_position = shift_amount + position     
          end_text += alphabet[new_position]
       else:
          end_text += char        
       
    print(f"{direction}d text is {end_text}")
    
       
    
ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter

#     print(f"The encoded text is {cipher_text}")


# encrypt(plain_text=text, shift_amount=shift)

# # dicrypting part
# def dycrypt(cipher_text=text, shift_amount=shift):
#     plain_text = ""
#     for letter in cipher_text:
#         position =alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded message is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     dycrypt(cipher_text=text, shift_amount=shift)



