#unindexed, unordered, no duplicates

set = {'one', 'two', 'three', 'three', 'three'}
subset = {'one', 'two', 'five', 'six', 'seven'}

set.add("four")
set.remove("one")
set.update(subset)
#set.clear()
new_set = set.union(subset)

for x in new_set:
    print(x)


print(set.difference(subset))