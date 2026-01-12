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
        usuarios_invalido = usuario
        usuarios_invalido["ERROR"]= 'Email invalido!'

print(usuarios_invalido["ERROE"] +" usuario: "+usuarios_invalido["nome"])

