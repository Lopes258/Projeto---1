import random
##Primeiro definir o esqueleto do jogo da velha
def display_tabuleiro(tabuleiro):
    
    print (tabuleiro[7]+' | '+tabuleiro[8]+' | '+tabuleiro[9])
    print ('----------')
    print (tabuleiro[4]+' | '+tabuleiro[5]+' | '+tabuleiro[6])
    print ('----------')
    print (tabuleiro[1]+' | '+tabuleiro[2]+' | '+tabuleiro[3])


teste_tabuleiro = [' ']*10
display_tabuleiro(teste_tabuleiro)

print("Bem Vindo ao JOGO DA VELHA")

##Segunda parte definir o input para o jogador decidir se ele quer começar como 'X' ou 'O'
def jogador_input():

    marcador = ""

    #Definir qual o Jogador 1 ira escolher entre X ou O

    while not (marcador == 'X' or marcador == 'O'):
        marcador = input('Jogador 1, escolha entre X ou O: ').upper()

    if marcador == 'X':
        return ('X','O')
    else:
        return ('O','X')

    #Passa para o Jogador 2 o marcador oposto


##Definir a posição do Marcador no tabuleiro
def local_marcador(tabuleiro, marcador, posicao):

    tabuleiro[posicao] = marcador

##Definir a função que vai marcar (X ou O) e checar se ganhou
def vencedor_check(tabuleiro, marca):

    # Vencer Jogo da velha

    #Checar todas as linhas

    return ((tabuleiro[7] == marca and tabuleiro[8] == marca and tabuleiro[9] == marca) or # horizontal topo
    (tabuleiro[4] == marca and tabuleiro[5] == marca and tabuleiro[6] == marca) or # horizontal meio
    (tabuleiro[1] == marca and tabuleiro[2] == marca and tabuleiro[3] == marca) or # horizontal inferior
    (tabuleiro[7] == marca and tabuleiro[4] == marca and tabuleiro[1] == marca) or # vertical da esquerda
    (tabuleiro[8] == marca and tabuleiro[5] == marca and tabuleiro[2] == marca) or # vertical do meio
    (tabuleiro[9] == marca and tabuleiro[6] == marca and tabuleiro[3] == marca) or # vertical da direita
    (tabuleiro[7] == marca and tabuleiro[5] == marca and tabuleiro[3] == marca) or # diagonal
    (tabuleiro[9] == marca and tabuleiro[5] == marca and tabuleiro[1] == marca)) # diagonal

## Determinar aleatoriamente qual dos jogadores começa primeiro
def escolher_primeiro():

    sorte = random.randint(0,1)

    if sorte == 0:
        return 'Jogador 1'
    else:
        return 'Jogador 2'

## Criar a função para determinar se o espaço no tabuleiro ainda esta disponivel
def checar_espaco(tabuleiro, posicao):

    return tabuleiro[posicao] == ' '
    

## Criar uma função para determinar se todo o tabuleiro esta cheio ou não
def checar_tabuleiro_cheio(tabuleiro):

    for i in range(1,10):
        if checar_espaco(tabuleiro, i):
            return False
    return True

##Função usada para que o jogador escolhar uma proxima posição sempre com um numero valido
def escolha_jogador(tabuleiro):

    posicao = 0
    
   
    while True:
        try:
        # Código que pode gerar uma exceção
            
            if posicao not in [1,2,3,4,5,6,7,8,9] or not checar_espaco(tabuleiro, posicao):
                posicao = int(input("Escolha uma posição : (1-9)"))
            return posicao
            
        
        # Se o código acima for bem-sucedido, saímos do loop
        except ValueError:
        # Se ocorrer uma exceção (por exemplo, ValueError), exibimos uma mensagem de erro
            print("Por favor, digite um número válido.")
            return posicao
        except KeyboardInterrupt:
        # Se o usuário pressionar Ctrl+C, interrompemos o programa
            print("\nPrograma encerrado pelo usuário.")
            break
            

##Criar uma função para determinar se o jogador que jogar novamente ou parar


#Juntar todos os codigos para rodar o jogo


while True:

    o_tabuleiro = [' ']*10
    jogador1_marcador,jogador2_marcador = jogador_input()
    turno = escolher_primeiro()

    print(turno + " Irá jogar primeiro")

    jogar = input("Pronto para jogar? S ou N: ").upper()

    if jogar == "S":
        jogue = True
    elif jogar == "N":
        break
    else:
         jogar = input("Pronto para jogar? S ou N: ").upper()


    while jogue:

        if turno == "Jogador 1":

            #Mostrar o tabuleiro
            display_tabuleiro(o_tabuleiro)
            #Escolher uma posição
            posicao = escolha_jogador(o_tabuleiro)
            #Colocar o marcador na posição
            local_marcador(o_tabuleiro,jogador1_marcador,posicao)
            #Checar se ganhou
            if vencedor_check(o_tabuleiro,jogador1_marcador):
                display_tabuleiro(o_tabuleiro)
                print("O JOGADOR 1 VENCEU!!")
                jogue = False
            else:
                if checar_tabuleiro_cheio(o_tabuleiro):
                    display_tabuleiro(o_tabuleiro)
                    print('EMPATE')
                    jogue = False
                
                else:
                    turno = 'Jogador 2'

        else:
            
            #Mostrar o tabuleiro
            display_tabuleiro(o_tabuleiro)
            #Escolher uma posição
            posicao = escolha_jogador(o_tabuleiro)
            #Colocar o marcador na posição
            local_marcador(o_tabuleiro,jogador2_marcador,posicao)
            #Checar se ganhou
            if vencedor_check(o_tabuleiro,jogador2_marcador):
                display_tabuleiro(o_tabuleiro)
                print("O JOGADOR 2 VENCEU!!")
                jogue = False
            else:
                if checar_tabuleiro_cheio(o_tabuleiro):
                    display_tabuleiro(o_tabuleiro)
                    print('EMPATE')
                    jogue = False
                
                else:
                    turno = 'Jogador 1' 

    def replay():

        escolha = input("Quer jogar de novo? Diga Sim ou Não: ").upper()

        if escolha == "Sim":
            escolha = True
        elif escolha == "Não":
            escolha = False
        else:
           escolha = input("Quer jogar de novo? Diga Sim ou Não: ").upper() 
        return escolha
    

    if not replay():
        break