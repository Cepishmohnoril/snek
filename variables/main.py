#str
first_name = "Doom"
last_name = "Guy"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))

#int
age = 21
age += 1
print("Your age is: " + str(age))
print(type(age))

#float
height = 175.5
print("Your height is: " + str(height) + "cm")
print(type(height))

#bool
human = False
print("Are you a human: " + str(human))
print(type(human))

#Mutli assignnment

one, two, three = 1, 2, 3
print(one, two, three)

one = two = three = 6
print(one, two, three)