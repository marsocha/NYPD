def odl2(a,b):
    return a*a + b*b

if __name__ == '__main__':
    print("ile iteracji?")
    n = int(input())
    print("co ile wypisywać?")
    wyp = int(input()) #co ile wypisywać?
    ile = 0 #ile razy trafilismy w kolo
    for i in range(1, n):
        a = random.uniform(0,2)
        b = random.uniform(0, 2)
        if odl2(a - 1,b - 1) < 1:
            ile = ile + 1
        if i % wyp == 0:
            print(ile/i * 4)
    print(ile/n * 4 - math.pi) #o ile się pomylilismy