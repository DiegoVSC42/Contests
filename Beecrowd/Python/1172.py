vetor = []
for i in range(0,10):
    vetor.append(0)
    

for i in range(0,10):
    x = int(input())
    
    if(x <= 0):
        vetor[i] = 1
    else:
        vetor[i] = x
        
for i in range(0,10):  
    print('X[%i] = %d'%(i,vetor[i]))