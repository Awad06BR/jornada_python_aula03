### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.


SENHA = "123@Mudar"
TENTATIVA = 3
qtd_tentativa = 0

senha = input("Informe a senha do administrador: ")


while senha != SENHA:
    qtd_tentativa+=1

    if qtd_tentativa < TENTATIVA:
        senha = input(f"Senha invalida. Por favor informe a senha do administrador:(tentativas restantes:{TENTATIVA-qtd_tentativa}) ")
    else:
        print("Usuario Bloqueado. Procure a equipe de TI!")
        exit()

print ("Usuario Logado. Seja Bem vindo(a)!")

        

