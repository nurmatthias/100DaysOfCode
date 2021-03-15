
from os import close


with open("day24/text.txt", mode="r") as file:
    content = file.read()
    print(content)

with open("day24/text.txt", mode="a") as file:
    file.write("\nNeuer Text...")

with open("day24/new_text.txt", mode="w") as file:
    file.write("Neuer Text...")