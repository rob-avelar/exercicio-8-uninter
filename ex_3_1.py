A = int(input('Digite o valor do primeiro lado '))
B = int(input('Digite o valor do segundo lado '))
C = int(input('Digite o valor do terceiro lado '))

if((A > 0 and B > 0 and C > 0) and (A + B > C and B + C > A)):

    if (A == B == C):
        print('Este triângulo é Equilátero')
    elif (A == B and A != C or A != B and A == C):
        print('Este triângulo é Isósceles')
    else:
        print('Este triângulo é Escaleno')

else:
    print('Algum dos lados não serve para formar um triângulo')