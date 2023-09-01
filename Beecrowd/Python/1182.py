M = []
for i in range(0,12):
    M.append([])
    for j in range (0,12):
        M[i].append(0)
C = int(input())

T = input()

for i in range(0,12):
    for j in range(0,12):
        M[i][j] = float(input())
cont = 0
for i in range(0,12):
    cont = cont + M[i][C]

if(T == "M"):
    cont = cont/12
print("%.1f"%cont)

