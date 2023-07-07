name = "doot Guy"

print(len(name))
print(name.find('t'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("y", "m"))
print(name * 3)


#Slice

first_name = name[:4] #0:4
print(first_name)

last_name = name[5:]
print(last_name)

dumm_name = name[::2]
print(dumm_name) #even bleed?

reverse_name = name[::-1]
print(reverse_name)

website = "https://goole.com"
slice = slice(8, -4)
print(website[slice])