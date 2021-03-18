#Exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [num**2 for num in numbers]

#Write your code 👆 above:

print(squared_numbers)



#Exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

#Write your code 👆 above:

print(result)



#Exercise 3
with open("day26/file1.txt") as file1:
    data1 = file1.readlines()

with open("day26/file2.txt") as file2:
    data2 = file2.readlines()

result = [int(num.strip()) for num in data1 if num in data2]

# Write your code above 👆

print(result)
