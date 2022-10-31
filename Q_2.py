nPessoas = int(input('Digite o numero de pessoas: '))
alturaMin = float(input('Digite a altura minima: '))
alturaMax = float(input('Digite a alutra maxima: '))

lista = []
pode = 0

for i in range(nPessoas):
    lista.append(float(input('digite sua altura: ')))

for i in range(len(lista)):
    if lista[i] >= alturaMin and lista[i] <= alturaMax:
        pode += 1

print(f'{pode} pessoas podem andar no brinquedo')
print(f'Todas as alturas: {lista}')

