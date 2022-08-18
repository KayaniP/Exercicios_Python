import random #random gera numeros aleatórios 

print('---------------------------------')
print ('Bem vindo ao jogo de advinhação!')
print('----------------------------------')

numero_secreto = random.randrange(1, 101) * 100
total_de_tentativas = 0
pontos = 1000

print("QUal nível de dificuldade você deseja?")
print("(1) Fácil (2)Médio (3)Difícil")
nivel = int (input("Defina o nível: "))
print ('numero secreto {}'.format(numero_secreto))
if(nivel ==1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10

else:
     total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute_str = input('Informe um número entre 1 e 100: ')
    print('Você digitou', chute_str)
    chute = int(chute_str)

    if (chute <1 or chute >100):
        print("Você deve digitar entre 1 e 100")
        #
#logica abaixo
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (acertou):
        print ('Você acertou e fez {} :) '.format(pontos))
        break #sai do laço

    else: 
        if (maior):
         print( 'Você errou, o seu chute foi maior do que o número secreto')
        elif(menor):
         print('Você errou, o seu chute foi menor que o número secreto')
        pontos_perdidos = abs(numero_secreto - chute) 
        pontos = pontos - pontos_perdidos

print ('fim do jogo :) ')    

#while = enquanto ainda há tentativas o código vai rodar