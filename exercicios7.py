def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial (num):
    """
    Função que calcula o fatorial de um número inteiro
    :param num: int: Número inteiro a ser calculado o fatorial
    :return: int: Fatorial do número

    """

    fat = 1
    if num == 0:
        return fat
    
    # Esta parte só é executada se num > 0

    for i in range(1, num + 1, 1):
        fat *=i
    return fat
    

# Programa principal

x = valida_int("Digite um valor para calcular a fatorial: ", 0, 9999)
print(f'{x}! = {fatorial(x)}')
