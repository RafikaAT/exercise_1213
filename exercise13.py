appending_file = open('pelican.txt', 'a')

first_line = appending_file.write('A wonderful bird is the pelican \n')
second_line = appending_file.write('His bill holds more than his belican \n')

list_lines = ['He can take in his beak, \n', 'Enough food for a week,\n', 'But I’m damned if I see how the helican.\n']

lines = appending_file.writelines(list_lines)

# \n requires to start new line

