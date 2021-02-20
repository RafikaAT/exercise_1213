cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
# print(cheese[4])
print(cheese)
# on line 2, Python is reading 'Oke' to be something like a list within itself,
# categorising each character as an item in the list. In order to
# overcome the problem, we must make Python classify Oke as a single item in a list,
# so we put square brackets around it.
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke']
cheese += ['Mozarella', 'Halloumi']
cheese.append('blue cheese')
cheese.extend(['Gouda'])
print(cheese)
