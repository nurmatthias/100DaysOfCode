# len(1234) wirft einen Fehler weil len() einen String erwartet

# Typprüfung
print(type(1234))

# Casting
a = 123
print(type(a))

a = str(a)
print(type(a))

a = float(a)
print(type(a))
