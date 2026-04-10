soma = 0

for c in range(6):
    numero = int(input('Digite os números: '))
    
    if numero % 2 == 0:
        soma = soma + numero

print(soma)
