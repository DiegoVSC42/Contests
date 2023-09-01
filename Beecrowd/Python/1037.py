A = 25
B = 50
C = 75
D = 100
read = float(input())

if(read < 0 or read > 100):
    print('Fora de intervalo')
elif(read <= A):
    print('Intervalo [0,25]')
elif(read <= B):
    print('Intervalo (25,50]')
elif(read <= C):
    print('Intervalo (50,75]')
elif(read <= D):
    print('Intervalo (75,100]')
