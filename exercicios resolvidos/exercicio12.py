### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.


numero = int(input ("informe um numero entre 1 e 5: "))

while numero < 1 or numero >5:
    numero = int(input ("Numero invalido! Por favor, informe um numero entre 1 e 5: "))

print("Numero valido!") 