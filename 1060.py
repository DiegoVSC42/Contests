read = input()
valores_int = [int(x) for x in read.split(" ")]

cont = 0

for i in range(0,7):
    valores_int[i] = input()
    if float(valores_int[i]) > 0:
        cont = cont + 1
        
print('%d valores positivos'%cont)