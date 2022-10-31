semana = {'segunda': [],
         'terça': [],
         'quarta':[],
         'quinta':[],
         'sexta':[],
         'sabado': [],
         'domingo': [] }

for i in semana:
    semana[i].append(input(f'Digite suas materias da {i} (separe-as por virgula): '))

for k, v in semana.items():
    print(f'{k}: {v}')

