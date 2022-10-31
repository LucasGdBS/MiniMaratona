lista = list()

for i in range(5):
    n = int(input('Digita um numero: '))
    if len(lista) == 0:
        lista.append(n)
        primeiro = n
    elif n >= primeiro:
        lista.insert(len(lista), n)
    elif n < primeiro:
        lista.insert(0, n)

print(lista)



