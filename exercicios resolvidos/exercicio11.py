### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

#entrada = input('')

#while entrada != 'sair':
##    entrada = input('')


dados = []
entrada =''

while entrada != 'sair':
    entrada = input("Digite um valor qualquer, ou sair para terminar a sessão:")
    if entrada != 'sair':
        dados.append(entrada)
        print (dados)
