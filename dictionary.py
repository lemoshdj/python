def dictadd (num):
    mydict={}
    for x in range(num):
        a = input('Введите ключ:')
        b = input('Введите значение:')
        mydict[a]=b
    print (mydict)

n = int(input('Сколько строк добавим в словарь:'))
dictadd(n)
