read = input()
valores_int = [int(x) for x in read.split(" ")]
A = valores_int[0]
B = valores_int[1]
C = valores_int[2]
D = valores_int[3]
if(B > C and D > A and (C+D) > (A+B) and C > 0 and D > 0 and A%2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')