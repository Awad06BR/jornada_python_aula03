### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.


lista = ['casa', 'apartamento', 'kitnet','sair','loft']

while True:
    for item in lista:
        if item.lower() == 'sair':
            exit()
        else:
            print(f"Processando item {item}")

        
        