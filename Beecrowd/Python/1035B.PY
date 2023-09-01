A = int(input())
B = int(input())
C = int(input())
D = int(input())
if(B > C):
    if(D > A):
        if((C+D) > (A+B)):
           if(C > 0):
                if(D > 0):
                    if(A % 2 == 0):
                        print('Valores aceitos')
else:
    print('Valores nao aceitos')

#RUNTIME ERROR#

