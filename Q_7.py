matrizA = [[], [], [], []]
matrizB = [[], [], [], []]
matrizC = [[], [], [], []]

for i in range(4):
    for j in range(4):
        matrizA[i].append(int(input(f'Digite o valor para matrizA [{i}][{j}]')))

for i in range(4):
    for j in range(4):
        matrizB[i].append(int(input(f'Digite o valor para matrizB [{i}][{j}]')))
        
for i in range(4):
    for j in range(4):
        matrizC[i].append(matrizA[i][j] + matrizB[i][j])

print(matrizC)