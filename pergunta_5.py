def inverte_texto(t):
    txt = ""
    for x in range(len(t)-1, -1, -1):
        txt += t[x]
    return txt

texto = input("Digite o texto que deseja inverter: ")

texto_rev = inverte_texto(texto)

print(texto_rev) 
