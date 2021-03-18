import pandas

#TODO 1. Create a dictionary in this format:
alphabet = pandas.read_csv("day26/nato_phonetic_alphabet.csv")

alpha_dict = {
    row.letter:row.code for (index, row) in alphabet.iterrows()
}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("What to translate? ").upper()

result = [alpha_dict[letter] for letter in word]
print(result)