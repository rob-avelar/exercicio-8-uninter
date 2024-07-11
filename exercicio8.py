def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso! \n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

# programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo não localizado no computador')
    criaArquivo(arquivo)
while True:
   print('MENU')
   print('1 - Cadastrar um novo item')
   print('2 - Listar os itens cadastrados')
   print('3 - Sair')
   
   op = valida_int('Escolha uma opção: ', 1, 3)
   if (op == 1): #Novo item
       print('Você esta cadastrando um novo item \n')
       nomeJogo = input('Nome do jogo: ')
       nomeVideogame = input('Nome do videogame: ')
       cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

   elif (op == 2): #Listar itens
       print('Você esta listando os itens cadastrados \n')
       listarArquivo(arquivo)
       
   else: #Sair
       print('Você saiu do programa \n')
       break