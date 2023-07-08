#Basic

def hello(first_name, last_name):
    print("Hello " + first_name + " " + last_name)
    print("Have a nice day!")

hello("Doot", "Guy")

f_name = "Dude"
l_name = "Duuuuude"

hello(f_name, l_name)

#Return

def multiply(n1, n2):
    return n1 * n2

result = multiply(20, 4)

print(result)

#Order

def order(one, two, three):
    print(one, two, three)

order(two=2, three=3, one=1)


#Scope

name = "Doot"

def printName():
    name = "Guy"
    print(name)

print(name)
printName()


#Multy args (tuples)

def sum(*args):
    sum = 0

    for i in args:
        sum += i

    return sum


print(sum(1, 2, 3, 4, 5))

#kwagrs (dictionary args)

def m_hello(**kwargs):
    for key, value in kwargs.items():
        print('Hello ' + value)

m_hello(first='Bro', second='Dude', third='Doot')