#Esse é um programa que visa lucrar com base em 10% da sua banca, um jeito de lucrar mais lentamente e deixando uma maior chance de voce não acabar o dia zerando sua banca
#caso queira operar ele com algo diferente dos 10% altere na linha 50 o valor "0.1" para quanto você ira operar (cada "0.1" é igual a 10%, ou seja, se você quiser ir pro all-win altere o valor para "1" = 100%  ou se quer ir com metade da banca, para "0.5" = 50%)
#Esse programa tambem opera com base na tabela de boringer mas não usa todo o lucro como seria normalmente -/- O PROGRAMA PODE NÃO ESTAR 100% CORRETO
from datetime import datetime
from datetime import date

data = datetime.now()
df=data.strftime('%d/%m/%Y %H:%M') #data com hora para usar nas operações de win e loss
dtf=data.strftime('%d/%m/%Y') #data sem hora para deixar na linha final com o rendimento e a banca

#DA LINHA 9 ATÉ A LINA 26 VOCÊ PODE APAGAR, ELA É MAIS UM INCENTIVO DO QUE ALGO REALMENTE NECESSÁRIO

# "a" é usado pra saber o total de lucro objetivo naquele dia (sabado e domingo não serão dias operaveis, descanse e aproveite a vida) (tentar alcançar cada "a" mensalmente)
a1=7.59 # necessario de 10x a + pra operar com esse valor ou seja 75.00
a2=57.64 # necessario de 10x a + pra operar com esse valor ou seja 580.00
a3=437.70 # necessario de 10x a + pra operar com esse valor ou seja 4380.00
a4=3323.78 # necessario de 10x a + pra operar com esse valor ou seja 33250.00
a5=25239.95 # necessario de 10x a + pra operar com esse valor ou seja 252400.00


print(f"10% de cada dia caso o lucro seja de 100% nas 10 tentativas\na1 = {a1:.2f}\na2 = {a2:.2f}\na3 = {a3:.2f}\na4 = {a4:.2f}\na5 = {a5:.2f}\n")
print(f"O lucro total possivel de cada dia é:\nD1 = {a1*10:.2f}\nD2 = {a2*10:.2f}\nD3 = {a3*10:.2f}\nD4 = {a4*10:.2f}\nD5 = {a5*10:.2f}\n")
print(f"caso o lucro seja minimo será: R${(a1)+(a2)+(a3)+(a4)+(a5):.2f} dol convertido pra reais fica: R${((a1)+(a2)+(a3)+(a4)+(a5))*5:.2f}\n\nOBS: Com o lucro minino o total mensal é: R${(((a1)+(a2)+(a3)+(a4)+(a5))*5)*4} em reais")
print(f"caso eu tenha sorte o lucro maximo da semana será: R${(a1*10)+(a2*10)+(a3*10)+(a4*10)+(a5*10):.2f} dol convertido pra reais fica: R${((a1*10)+(a2*10)+(a3*10)+(a4*10)+(a5*10))*5:.2f}\n\nOBS: Com o lucro maximo o total mensal é: R${(((a1*10)+(a2*10)+(a3*10)+(a4*10)+(a5*10))*5)*4:.2f} em reais")
print(f"Objetivo é 1 dos a1={a1*10:.2f} a2={a2*10:.2f} a3={a3*10:.2f} a4={a4*10:.2f} a5={a5*10:.2f} por semana")
print("Não precisa ser hoje nem amanhã, mas um dia o objetivo é alcançado")
print("AJA COM CALMA E CONFIE NO SEU SONHO QUE VOCÊ IRA ALCANÇAR O SUCESSO 100% DE CERTEZA.\n")

#DA LINHA 9 ATÉ A LINA 26 VOCÊ PODE APAGAR, ELA É MAIS UM INCENTIVO DO QUE ALGO REALMENTE NECESSÁRIO

#definição das variaveis
loop = 0 # define quantas repetições o programa ira executar antes de se auto encerrar
entrada = 0 # para a primeira entrada sempre será 10% do valor da banca
i=1 # contador para interromper caso aja muitas vitorias consecultivas
win=0 # armazena o valor total da win
loss=0 # armazena o valor da loss
rendimento=0 # soma de win e loss
banca_final = 0 
stop_loss = 0 # contador de derrotas para que não acabe zerando a banca de uma vez

#abre o arquivo em que ficara salvo as informações
bd = open('Gerenciamento.txt','a') 


banca_inicial=float(input("Digite o valor da sua banca: R$")) # valor disponivel para seu investimento
bd.write(f"{dtf} - Banca Inicial: R${banca_inicial}\n")
#inicio do loop, altere o numero '1' para quantos loops você desejar
while loop < 5:
    loop+=1
    #verifica se tem o minimo necessario para operar
    if banca_inicial < 1:
        print(f"\nImpossivel operar com esse valor!\n")
        break
    else:
        entrada = banca_inicial*0.1
        print(f"\nVocê deve operar com R${entrada}\n")
        escolha = int(input("Você ganhou? digite 1 para sim e 0 para não\n"))
        #escolha de vitoria derrota
        while escolha == 1: # caso ganhe
            i+=1
            win = (entrada*1.92)-entrada # lucro de 92%
            entrada = entrada*1.5 # entrada equivalente a entrada anterior mutiplicado por 1.5 (50%)
            rendimento+=win # acrescenta o lucro ao rendimento
            bd.write(f"Entrada: R${entrada:.2f}\nWin: R${win:.2f}\n") #escreve no arquivo de texto o valor de entrada e o valor do lucro
            print(f"Você deve usar para próxima operação R${entrada:.2f} na {i}° vez")
            escolha = int(input("Você ganhou? digite 1 para sim e 0 para não\n"))
            if i == 5 and escolha == 1: # caso voce ganhe até a ultima vez a entrada não é perdida, logo é acrescentada ao rendimento
                rendimento+=entrada
            if escolha == 0 : # caso perca
                i=1 # reseta o contador de wins consecultivas
                loss-=entrada # acrescenta a entrada negativa na loss
                rendimento+=loss # Faz a soma da perca sobre o rendimento
                bd.write(f"Loss: R${loss:.2f}\n")
                #reset de win e loss para que não interfira no próximo loop
                win = 0 
                loss = 0
                stop_loss+=1 #acrescenta a derrota
                # encerra o loop de escolha
            if i==5:
                i=1
                print(f"Parabens, você ganhou muito!\n")
                #reset de win e loss para que não interfira no próximo loop
                win = 0
                loss = 0
                #reset do stop loss
                stop_loss=0
                break
        if escolha ==0:
            loss-=entrada # acrescenta a entrada negativa na loss
            rendimento+=loss # Faz a soma da perca sobre o rendimento
            bd.write(f"Entrada: R${entrada:.2f}\nLoss: R${loss:.2f}\n")
            #reset de win e loss para que não interfira no próximo loop
            win = 0 
            loss = 0
            stop_loss+=1 #acrescenta a derrota
            # encerra o loop de escolha
        if loop == 1 and escolha == 0:
            print("Derrota na primeira operação não da, volta amanha.\n")
            break
        if stop_loss == 3:
            print(f"Você ja perdeu o suficiente por hoje, vá descansar.\n")
            break


banca_final +=  rendimento + banca_inicial # faz a soma para mostrar quanto ficou na sua banca após o lucro/Perca

bd.write(f"\n{dtf} - Rendimento: R${rendimento:.2f} / Banca Final: R$ {banca_final:.2f}\n-------------------------------------------------------\n")
bd.close()

