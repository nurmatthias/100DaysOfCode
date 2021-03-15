#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#read all names
with open("day24/mailMerge/Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

with open("day24/mailMerge/Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

    for name in names:
        new_letter = letter.replace("[name]", name.strip())
        file_name = f"day24/mailMerge/Output/ReadyToSend/letter_for_{name}.txt"
        with open(file_name, mode="w") as file:
            file.write(new_letter)
