import random

x = random.randint(1, 10)
y = random.random()

print(x, y)

list = ['one', 'two', 'three']
z = random.choice(list)

print(z)

cards = [1, 2, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)

print(cards)