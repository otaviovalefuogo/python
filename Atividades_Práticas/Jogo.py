print("--------------------------------------------------")
print("---- Jogo Pedra,Papel e Tesoura (2 jogadores) ----")
print("--------------------------------------------------\n\n")
opcoes_validas=("pedra","papel","tesoura")
print(f"Opções válidas: {opcoes_validas}")
print("Dica: Digite 'sair' a qualquer momento para encerrar o jogo.\n")
j1=0
j2=0
while True:
    print("-"*50)
    jogada_inicialJ1=input("Jogador 1 digite sua jogada: ")
    jogadaJ1=jogada_inicialJ1.lower().strip()
    if jogadaJ1=="sair":
        print("Jogo encerrado")
        break
    jogada_inicialJ2=input("Jogador 2 digite sua jogada: ")
    jogadaJ2=jogada_inicialJ2.lower().strip()
    if jogadaJ1=="sair":
            print("Jogo encerrado")
            break
    print("\n")

    if jogadaJ1 not in opcoes_validas or jogadaJ2 not in opcoes_validas:
        print("ERRO: Uma ou ambas as jogadas são inválidas.\nDigite apenas 'pedra','papel' ou 'tesoura'")
    elif jogadaJ1==jogadaJ2:
        print("Resultado da rodada: Empate")
    elif jogadaJ1=="pedra" and jogadaJ2=="tesoura" or jogadaJ1=="papel" and jogadaJ2=="pedra" or jogadaJ1=="tesoura" and jogadaJ2=="papel":
        print("Resultado da rodada: Jogador 1 Venceu")
        j1+=1
    else:
        print("Resultado da rodada: Jogador 2 Venceu")
        j2+=1
    print(f"Pontuação\nJogador 1: {j1}\nJogador 2: {j2}\n")
    