print('Esses são os produtos disponíveis:')
print('Coxinha - R$ 5,00')
print('Pastel - R$ 7,00')
print('Café - R$ 4,00')
print('Suco - R$ 6,00')
print('SAIR - Para finalizar a compra')

total = 0
while True:
    op = int(input('Qual item gostaria de comprar? '))
    qtd = int(input('Quantas unidades gostaria de comprar? '))

    if (op == 1):
        total = total + 5 * qtd

    elif (op == 2):
        total = total + 7 * qtd
    elif (op == 3):
        total = total + 4 * qtd
    elif (op == 4):
        total = total + 6 * qtd
    elif (op == 5):
        break
        
    else:
        print('Produto inválido. Selecione outro.')

print(f'O total da sua compra é: R$ {total:.2f}')