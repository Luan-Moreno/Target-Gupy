entrada = int(input("Digite o número desejado: "))
lista = []

def fibonacci(x):
    if(x < 2):
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
global verifica
verifica = False

for z in range(0, entrada+1):
    print(f"{fibonacci(z)}", end=" ")
    if(fibonacci(z) == entrada):
        print(f"\n{entrada} pertence a sequência")
        verifica = True
        break

if(verifica == False):
    print(f"\n{entrada} não pertence a sequência")