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
        return 0

# Chamando a função calculadora
resultado = calculadora(6, 7, 3)

# Saída de dados
print(f"O resultado da operação é: {resultado}")
