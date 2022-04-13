x = int(input())

vetor = []
for i in range(0,10):
    vetor.append(0)
vetor[0] = x
for i in range(1,10):
    vetor[i] = vetor[i-1] * 2

for i in range(0,10):  
    print('N[%i] = %d'%(i,vetor[i]))