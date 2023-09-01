import math

read = input()
valores_int = [float(x) for x in read.split(" ")]
A = valores_int[0]
B = valores_int[1]
C = valores_int[2]
delta = math.pow(B,2) - 4*A*C

if(delta < 0 or A == 0):
    print('Impossivel calcular')
else:
    R1 = (-B+math.sqrt(delta))/(2*A)
    R2 = (-B-math.sqrt(delta))/(2*A)
    print('R1 = %.5f' %R1)
    print('R2 = %.5f' %R2)
