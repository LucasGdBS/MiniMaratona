gabarito = []
alunos = {'identificador': 0}
listaAlunos = []

for i in range(10):
    gabarito.append(input(f'questão {i+1}: Digite a resposta: (a, b, c, d, e)'))

while idy == 5:
    idy = int(input('Digite o ID do aluno: '))
    alunos['identificador'] = idy
    
    listaAlunos = alunos
