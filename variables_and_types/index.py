name = "doot Guy!"

if(name[0].islower()):
    print(name.capitalize())

first_name = name[:4].upper()
last_name = name[5:-1].lower()
last_character = name[-1]


print(first_name)
print(last_name)
print(last_character)