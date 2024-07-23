'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e 
continuará perguntando até que um valor correto seja preenchido.
'''

def calcular_idade(ano_nascimento, ano_atual=2022):
    return ano_atual - ano_nascimento

while True:
    try:
        nome_completo = input("Digite seu nome completo: ")
        ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
        
        if 1922 <= ano_nascimento <= 2021:
            idade = calcular_idade(ano_nascimento)
            print(f"Nome: {nome_completo}, Idade em 2022: {idade} anos")
            break
        else:
            print("Erro: O ano de nascimento deve estar entre 1922 e 2021. Tente novamente.")
    except ValueError:
        print("Erro: Você deve digitar um número válido para o ano de nascimento. Tente novamente.")


