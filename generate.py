import random
def generator(min,max):
    num=''
    for x in range(10):
        num=num+str(random.randint(int(min),int(max)))
    print('Результат:', num)

print('Генератор длинного числа')
imin=input('Min:')
imax=input('Max:')
generator(imin,imax)