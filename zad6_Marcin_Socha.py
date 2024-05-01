import os
import random
import string

week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
pory = ['mor', 'eve']

def initial():
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
initial()

def search_hard(path, ret):
    for folder in os.listdir(path):
        new_path = os.path.join(path, folder)
        if os.path.isfile(new_path):
            f = open(new_path, "r")
            f.readline()
            if (f.read(1)) == 'A':
                while (f.read(1) != ';'):
                    pass
                while (f.read(1) != ';'):
                    pass
                (f.read(1))
                tmp = f.read(1)
                if tmp.isdigit():
                    tmp2 = int(tmp)
                sum_tmp = 0
                while tmp.isdigit():
                    # print(tmp)
                    sum_tmp *= 10
                    sum_tmp += tmp2
                    tmp = (f.read(1))
                    if tmp.isdigit():
                        tmp2 = int(tmp)
                print(sum_tmp)
                ret.append(sum_tmp)
        else:
            search_hard(new_path, ret)

retu = []
path = os.path.join(os.getcwd(), 'week/')
search_hard(path, retu)
print(sum(retu))
def search_easy():
    ret = 0
    for day in week:
        for when in pory:
            path = os.path.join('./week/', day, when)
            path_file = os.path.join(path, 'Solution.csv')
            with open(path_file, "r") as f:
                f.readline()
                if f.read(1) == 'A':
                    #print(f.read(3))
                    while (f.read(1) != ';'):
                        pass
                    while(f.read(1) != ';'):
                        pass
                    f.read(1) #dodatkowa spacja
                    tmp = f.read(1)
                    if tmp.isdigit():
                        tmp2 = int(tmp)
                    sum_tmp = 0
                    while tmp.isdigit():
                        #print(tmp)
                        sum_tmp *= 10
                        sum_tmp += tmp2
                        tmp = (f.read(1))
                        if tmp.isdigit():
                            tmp2 = int(tmp)
                    print(sum_tmp)
                    ret += sum_tmp
    print(ret)
