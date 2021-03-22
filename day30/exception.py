#FileNotFound
#with open("a_file.txt") as file:
#    file.read()

#KeyError
#a_dict = {"key": "value"}
#value = a_dict["non_existing_key"]

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    value = a_dict["non_existing_key"]
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exists.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height**2
print(bmi)