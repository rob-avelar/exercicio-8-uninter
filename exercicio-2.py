km = int(input('Quantos kilometros você percorreu com o carro alugado? '))
dia = int(input('Por quantos dias você alugou o carro? '))
preco = dia*60 + 0.15*km
print(f'O preço total a ser pago são: R$ {preco}')