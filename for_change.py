import random, array

def randlist():
    arr=[]
    for a in range(10):
        arr.append(random.randint(10,100))
    return arr

list = randlist()
print (list)
chnum = input('Какой элемент в списке будем менять (от 0 до 9)?')
list[int(chnum)]=int(chnum)
print ('Новый список\n',list)