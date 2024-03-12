def juz_byl(list_of, num):
    ile = 0
    while num in list_of and ile < 2:
        print('ktos juz podal taki numer, podaj jeszcze raz \n lub napisz \'nie\'')
        print('jak wpiszesz 3 razy zly numer zaczniemy od poczatku grrr')
        num = str(input())
        ile += 1
    if num != 'nie' and ile != 2:
        list_of.append(num)
        ret = 1
    else:
        print('ehhhh, wpisz imie, chyba, ze juz nie chcesz, to napisz \'end\'')
        ret = 0
        
    return ret
  
def dodatkowo():
    dod = 'tak'
    while dod == 'tak':
        print('chcesz cos dodac? \n jak tak to napisz co \n jesli nie, to napisz \'nie\'')
        dod = str(input())
        if dod != 'nie':
            new_num = str(input())
            juz_byl(list_of_numbers, new_num)
            tmp = [dod, new_num]
            phone_book[names].append(tmp)
            dod = 'tak'
        else:
            print('to teraz nastepna osoba')         


if __name__ == '__main__':
    
    list_of_numbers = []
    phone_book = {}
    end = 0
    while not end:
        print('wpisz imie, chyba, ze juz nie chcesz, to napisz \'end\'')
        fn = str(input())
        if fn == "end": end = 1
        else:
            sn = str(input())
            num = str(input())
            udalo_sie = juz_byl(list_of_numbers, num)
            if udalo_sie:
                names = (fn, sn)
                phone_book[names] = ['main', num]
                dodatkowo()

    print(phone_book)
