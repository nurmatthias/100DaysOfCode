from caeserCipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shift_amount, cypher_direction):
    end_text = ""
    alphabet_len = len(alphabet)

    if cypher_direction == "decode":
        shift_amount *= -1

    for char in start_text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount

            if new_position >= alphabet_len:
                    new_position = (alphabet_len - new_position) * -1
            elif new_position < 0:
                    new_position = alphabet_len - (new_position * -1)
            
            end_text += alphabet[new_position]
        
        else:
            end_text += char
    
    print(f"The {cypher_direction}d text is {end_text}")
    

print(logo)

run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caeser(text, shift, direction)

    run_again = input("Restart the program? y/n ").lower()
    if run_again == "n":
        run = False
        print("Goodbye!")

