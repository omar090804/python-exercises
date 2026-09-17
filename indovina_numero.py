import random

print('primo prog')
n = random.randint(1, 6)
indovinato = False

for i in range(4):
    number = int(input('indovina il numero tra 1 e 6 (hai 4 possibilita) ?'))

    if n > number:
        print('il numero e piu alto ')
    elif n < number:
        print('il numero e piu basso')
    else:
        print('hai indovinato')
        indovinato = True
        break

if not indovinato:
    print('hai perso')
