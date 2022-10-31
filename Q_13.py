listaCerta = []

n = int(input())

for i in range(n):
    cadeia = input().upper()
    cadeiaTeste = input().upper()

    cadeiaCerta = ''

    for i in cadeia:
        if i == 'T':
            cadeiaCerta += 'A'
        elif i == 'A':
            cadeiaCerta += 'T'
        elif i == 'C':
            cadeiaCerta += 'G'
        else:
            cadeiaCerta += 'C'
    
    if cadeiaTeste == cadeiaCerta:
        listaCerta.append('COMPLEMENTARES')
    else:
        listaCerta.append('NAO COMPLEMENTARES')
        listaCerta.append(cadeiaCerta)

for i in listaCerta:
    print(i)
