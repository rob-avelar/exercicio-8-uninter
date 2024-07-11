nome = (input('Qual é o seu nome? '))

if (nome == 'Vinicius'):
    print('Vinicius')
else:
    idade = int(input('Qual a sua idade? '))
if (idade <= 18):
    print(f'Você é menor de idade')
elif (idade >= 100):
    print(f'Você possívelmente não existe')   
else:
    print('Obrigado pela confirmação')