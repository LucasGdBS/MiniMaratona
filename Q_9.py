materias = int(input('Digite a quantidade de materias: '))
ira = 0
cargasTotais = 0

for i in range(materias):
    notas = float(input('Digite a nota da disciplina'))
    cargaHoraria = (float(input('Digite a carga horária dessa disciplina: ')))
    ira += notas*cargaHoraria
    cargasTotais += cargaHoraria

print(f'O IRA é: {ira/(cargasTotais*100)}')