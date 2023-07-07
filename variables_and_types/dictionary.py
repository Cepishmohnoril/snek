languages = {'usa': 'english', 'germany': 'deutsch', 'france': 'french', 'ukraine': 'ukrainian'}

print(languages['usa'])
print(languages.get('germany'))
print(languages.keys())
print(languages.values())
print(languages.items())

languages.update({'usa': 'american'})
languages.pop('france')
#languages.clear()

for key,value in languages.items():
    print(key + ":" + value)