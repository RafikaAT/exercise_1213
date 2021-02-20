import random
help(random)

lottery = []
# count = 0
# for i in lottery, count<6:
#    i = [random.randrange(1, 51)]
#    lottery.append(i)
#    count +=1
#    print(lottery)
#    print(count)
#
# for i in lottery, count<6:
#     i = random.randint(1, 50)
#     lottery.append(i)
#     count +=1
# print(lottery)

for i in range(6):
    i = random.randint(1, 50)
    lottery.append(i)
print(lottery)