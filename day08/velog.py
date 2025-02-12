from collections import Counter

lst = ['apple', 'apple', 'banana', 'orange', 'mango','mango', 'mango']
count = Counter(lst)
print(count)
s_count = Counter('banana')
# Counter({'mango': 3, 'apple': 2, 'banana': 1, 'orange': 1})
print(s_count)
print(s_count.most_common())
print(f'과일 개수top3: {count.most_common(3)}')
print(f'과일 개수 top1: {count.most_common(3)[0]}')
print(f'가장 많은 과일은?: {count.most_common(3)[0][0]}')
print(f'가장 많은 과일의 수는?: {count.most_common(3)[0][1]}')
print(count.most_common(1)[0])
print(count.most_common(1)[0][0])
print(count.most_common(1)[0][1])



print(list(count.elements()))
# ['apple', 'apple', 'banana', 'orange', 'mango', 'mango', 'mango']


print(count.keys())
print(count.values())
print(count.items())
# dict_keys(['apple', 'banana', 'orange', 'mango'])
# dict_values([2, 1, 1, 3])
# dict_items([('apple', 2), ('banana', 1), ('orange', 1), ('mango', 3)])
print()
count.update(['melon', 'melon'])
print(count)
count.subtract(['mango'])
print(count)

print()
a = Counter('apple')
b = Counter('pineapple')
print(a+b)
print(a-b)
print(b-a)
# Counter({'p': 5, 'e': 3, 'a': 2, 'l': 2, 'i': 1, 'n': 1})
# Counter()
# Counter({'p': 1, 'i': 1, 'n': 1, 'e': 1})

a.subtract(b)
print(a)