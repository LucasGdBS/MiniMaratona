tupla = ('lucas', 'gabriel', 'guilherme', 'carol', 'matheus')
vogais = ('a', 'e', 'i', 'o', 'u')
vogaisPalavra = []

for i in tupla:
    for j in i:
        if j in vogais:
            vogaisPalavra.append(j)
    print(f'Na palavra {i} as vogais são {vogaisPalavra}')
    vogaisPalavra.clear()