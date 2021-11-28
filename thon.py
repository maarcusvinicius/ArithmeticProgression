from time import sleep
print('=' * 33)
print('{:^40}'.format('\033[31m10 TERMOS DE UMA PA\033[m'))
print('=' * 33)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print('{} -> '.format(termo), end=(''))
        termo += razao
        cont += 1
    print('PAUSA')
    sleep(1)
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Voce utilizou \033[0;32m{} termos\033[m'.format(cont))
