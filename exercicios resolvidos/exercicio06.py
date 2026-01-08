### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = input("Escreva um pequeno texto: ").upper()#Colocar letra em maiusculo para não repetir
palavras = texto.split()

contagem = {}

for x in palavras:# a cada palavra
    if x in contagem:# verificar a existencia em contagem
        contagem[x]+=1# se existir incrementa mais um
    else:
        contagem[x]=1 #se não adiciona e conta 1

print(contagem)
