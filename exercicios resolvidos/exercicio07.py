### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

##Formula de normalização = [(x - min(numeros)) / (max(numeros) - min(numeros))

##Metodo Pratico
#numeros = [10,20,30,40,50]
#numero_minimo = min(numeros)
#numero_maximo = max(numeros)
#normalizados = [(x - min(numeros)) / (max(numeros) - min(numeros)) for x in numeros]
#print(normalizados)


numeros = [10,20,30,40,50]
normalizados = []


for numero in numeros:
    normalizado = (numero - min(numeros)) / (max(numeros) - min(numeros))
    normalizados.append(normalizado)

print(normalizados)





