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

#format
#And many more other stuff
#Check str.format() python documentations for details

nameVar = "Doot Guy"
text = "Hello my name is {}"
text2 = "Hello my name is {0}"
text3 =  "Hello my name is {name}"

print(text.format(nameVar))
print(text2.format(nameVar))
print(text3.format(name=nameVar))

n = 1000

print("The number is {:.3f}".format(n))
print("The number is {:,}".format(n))
print("The number is {:b}".format(n))
print("The number is {:o}".format(n))
print("The number is {:X}".format(n))
print("The number is {:E}".format(n))