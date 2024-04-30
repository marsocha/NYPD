import os
import random
import string

week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
pory = ['mor', 'eve']

for day in week:
    for when in pory:
        path = os.path.join('./week/', day, when)
        os.makedirs(path)
        path_file = os.path.join(path, 'Solution.csv')
        os.mknod(path_file)
        with open(path_file, "w") as file:
            file.write("Model; Output value; Time of computation; \n")
            first = str(random.choice(('A', 'B', 'C')))
            second = str(random.choice(range(0,1000,1)))
            third = str(random.choice(range(1,1000,1))) + 's'
            file.write(first + '; ' +  second + '; ' + third)

def search_tmp(path):
    for folder in os.listdir():
        if os.path.isfile(folder):
            f = open(folder, "r")
            f.readline()
            if (f.read(1)) == 'A':
                while (f.read(1) != ';'):
                    pass
                while (f.read(1) != ';'):
                    pass
                print(f.read(2))
                print('aaa')
        else:
            search(os.path.join(path, folder))


ret = 0
for day in week:
    for when in pory:
        path = os.path.join('./week/', day, when)
        path_file = os.path.join(path, 'Solution.csv')
        with open(path_file, "r") as file:
            f.readline()
            if f.read(1) == 'A':
                while (f.read(1) != ';'):
                    pass
                while (f.read(1) != ';'):
                    pass
                tmp = int(f.read(1))
                sum_tmp = 0
                while tmp != ';':
                    sum_tmp *= 10
                    sum_tmp += tmp
                    tmp = int(f.read(1))
                ret += sum_tmp
print(ret)
