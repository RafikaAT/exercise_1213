read_pelican = open('pelican.txt').read()
print(read_pelican)
print(type(read_pelican))

list_pelican = open('pelican.txt').read().splitlines()
print(list_pelican)
print(len(list_pelican))

for i in list_pelican:
    print(i)