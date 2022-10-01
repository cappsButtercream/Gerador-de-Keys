import random
from time import sleep

file = open('tokens criados', 'r+')
f = file.read()

t = ''
a = True
token = list()

alfabeto = ('q', 'w', 'e', 'r', 't', 'y', 'u',
            'i', 'o', 'p', 'a', 's', 'd', 'f',
            'g', 'h', 'j', 'k', 'l', '8', 'z',
            'x', 'c', 'v', 'b', 'n', 'm', '0')

print('[gerador de tokens aleatorios]')
sleep(2)
print('\nObtenha seus NFTs aqui!')
sleep(1.7)
print('wanna mokey? you can get it!')
sleep(2)
v = str(input('\nIniciar processo? [S/N]: '))

if v.lower() == 's':
    while a:
        for c in range(0, 7):
            while True:
                r = random.choice(alfabeto)
                if r in token:
                    r = random.choice(alfabeto)
                else:
                    token.append(r)
                    break

        t = f'{token[0]}{token[1]}{token[2]}{token[3]}{token[4]}{token[5]}{token[6]}'

        while True:
            if t in f:
                print('[*COLISÃO_DE_DADOS*]')
                break
            else:
                file.write(f'{t}\n')
                sleep(1)
                print('\nToken criado!')
                sleep(0.5)
                print(f'Token: {t}')
                a = False
                break