#Ordered and unchangable


tuple = ('Tony', 30, 'male')

print(tuple.count('Tony'))
print(tuple.index('Tony'))

for f in tuple:
    print(f)

if 'male' in tuple:
    print('Male tuple')