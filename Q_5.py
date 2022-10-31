nome1 = input('Digite seu nome: ')
nome2 = input('Digite seu nome: ')

op = input(f'{nome1} escohe ímpar ou par? ')

numero1 = int(input(f'{nome1} digite seu numero: '))
numero2 = int(input(f'{nome2} digite seu numero: '))

resposta = numero1 + numero2

if resposta%2 == 0:
    if op.lower() == 'par':
        print(f'{nome1} você ganhou!!')
else:
    print(f'{nome2} você ganhou!!')
