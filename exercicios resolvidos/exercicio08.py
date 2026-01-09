### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]


usuarios_invalido = []

for usuario in usuarios:
    if usuario["email"] == '': 
        usuarios_invalido.append(usuario)

print(usuarios_invalido)

###Pendencia
# Adicionar a mensagem de erro a ser apresentada. O erro deve ser gravado no log (Dicionario:usuarios_invalido)
