programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# Adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}


# Loop
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
}