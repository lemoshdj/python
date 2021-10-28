import random, array
def search(number, array):
    y=0
    for x in array:
        if int(x)==int(number):
            print ('Число',number,'находится под номером', y)
        y=y+1


arrayn=[]
for x in range(10):
    arrayn.append(random.randint(0,10))
print(arrayn)
numb=input('Какое число ищем?')
search(numb,arrayn)