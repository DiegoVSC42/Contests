M = []
for i in range(0,12):
    M.append([])
    for j in range (0,12):
        M[i].append(0)
O = input()
for i in range(0,12):
    for j in range(0,12):
        M[i][j] = float(input())
cont = 0
for i in range(0,12):
    for j in range(0,12):
        if(i > j):
            cont = cont + M[i][j]

if(O == "M"):
    cont = cont/66
    
print("%.1f"%cont)