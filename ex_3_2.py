kwh = float(input('Qual a quantidade de kWh consumido? '))
tipo = input('Qual o tipo de instalação? Digite R para residências, I para indústrias e C para comércios ')

if(tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
    print(f'Total a pagar: R$ {kwh * preco}')    


elif(tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
    print(f'Total a pagar: R$ {kwh * preco}') 

elif(tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
    print(f'Total a pagar: R$ {kwh * preco}') 

else:
    print('Instalação inválida. Encerrando...')