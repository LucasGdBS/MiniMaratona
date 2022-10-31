tempoPresente = float(input('Digite quanto tempo precisa para fazer um presente em minutos: '))
tempoRestante = float(input('Digite quanto tempo falta para acabar o dia em minutos: '))

if tempoPresente*2 <= tempoRestante:
    print('Corre que da tempo!')
else:
    print('Sinto muito, deixa pra amanhã')

