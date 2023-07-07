doot = ['bfg', 'chainsaw', 'super shotgun']

doot[1] = 'boomstick'
doot.append('machinegun')
doot.remove('bfg')
doot.pop()
doot.insert(3, 'bfg')
doot.sort()
#doot.clear()


for x in doot:
    print(x)


#2D list

x = [1, 2, 3]
y = [4, 5, 6]
z = [x, y]

print(z[1][2])