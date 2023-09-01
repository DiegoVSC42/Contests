vetor = []
for i in range(0,100):
    vetor.append(0)
for i in range(0,100):
    vetor[i] = float(input())
for i in range(0,100):
    if(vetor[i] <= 10):
        print("A[%d] = %.1f"%(i,vetor[i]))