'''
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. 
Depois precisa executar a operação e mostrar o resultado na tela. 
Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
'''

# Definindo a função calculadora
def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2
    else:
        return "Essa opção não existe"

# Loop infinito para a calculadora
while True:
    # Mostrando o menu de operações
    print("\nEscolha a operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    
    # Lendo a operação escolhida pelo usuário
    operacao = int(input("Digite o número para a operação correspondente: "))
    
    # Verificando se o usuário escolheu sair
    if operacao == 0:
        print("Saindo...")
        break

    # verificando se a opção é válida
    if operacao not in [1, 2, 3, 4]:
        print("Essa opção não existe")
        continue
    
    # Lendo os números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Chamando a função calculadora e exibindo o resultado
    resultado = calculadora(num1, num2, operacao)
    print(f"Resultado: {resultado}")
