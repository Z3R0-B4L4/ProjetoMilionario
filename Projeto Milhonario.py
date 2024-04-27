#Esse é um programa que visa lucrar com base em 10% da sua banca, um jeito de lucrar mais lentamente e deixando uma maior chance de voce não acabar o dia estourando sua banca
#caso queira operar ele com algo diferente dos 10% altere na linha 49 o valor "0.1" para quanto você ira operar (cada "0.1" é igual a 10%, ou seja, se você quiser ir pro all-win altere o valor para "1" = 100%  ou se quer ir com metade da banca, para "0.5" = 50%)
#Esse programa tambem opera com base na tabela de boringer mas não usa todo o lucro como seria normalmente -/- O PROGRAMA AINDA ESTÁ EM DESENVOLVIMENTO

from datetime import datetime
from datetime import date

data = datetime.now() # captura a data e horario atual
df=data.strftime('%d/%m/%Y %H:%M') # formata a data para o padrão brasileiro e mostra o horario junto
dft=data.strftime('%d/%m/%Y') # formata a data para o padrão brasileiro (data especifica para o total)

loop = 0 
d1 = 0 # "d" = dia
i=1 # "i" um contador para por limite
w = 0 # win de cada dia
l = 0 # loss de cada dia
rendimento = 0 # rendimento de cada operação
banca = 0 # banca de cada dia
x = 0 # mutiplicador para o break do stop loss
bd = open('Gerenciamento.txt','a') # bd é tipo um banco de dados, ele utiliza a função open para abrir o aquivo txt com nome Gerenciamento e o parametro "a" que ele recebe após a virgula é para que caso algo seja adicionado nele, que seja adicionado no final do documento

# "a" é usado pra saber o total de lucro objetivo naquele dia (1 = segunda, 2 = terça, 3 = quarta, 4 = quinta, 5 = sexta, sabado e domingo não serão dias operaveis, descanse e aproveite a vida)
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

s=float(input("Digite sua banca: ")) # <--- BANCA ---><--- BANCA ---><--- BANCA ---><--- BANCA ---><--- BANCA ---><--- BANCA ---><--- BANCA ---><--- BANCA ---><--- BANCA --->
bd.write(f"{dft} - Banca Inicial: {s}\n")
while True:
    loop +=1
    if loop > 10:
        break 
    print(f"{loop}° loop ")
    if s < 1: # operação minima é 1$
        print("Pobre, vaza") # Não se ofenda, é só uma brincadeira
        break
    p = int(input("Digite 1 para prosseguir\n"))
    if p==1:
        d1=s*0.1 # 10% da banca
        print(f"Você deve usar {d1:.2f}")
        bd.write(f"{df} Entrada de: R${d1:.2f}\n")
        opt = int(input("Você ganhou? 1 para sim 0 para não: "))
        if opt == 0:
            l += l - d1
            rendimento += l+d1
            banca += l
            bd.write(f"{df} - loss: R${round(l,2)}\n")
            l = 0
        while opt == 1:
            d1 = d1*1.5
            i += 1
            print(f"Você deve usar {d1:.2f} para a {i}° vez\n")
            opt = int(input("Você ganhou? 1 para sim 0 para não: "))
            if opt == 1:
                w += d1*1.92 # Lucro de 92%
                rendimento += w-d1
                banca += rendimento+l
                bd.write(f"{df} - win: R${round(w,2)}\n")
            elif opt == 0:
                w += d1*1.92
                l += l - d1
                rendimento += w-d1
                banca += rendimento+l
                bd.write(f"{df} - win: R${round(w,2)}\n")
                bd.write(f"{df} - loss: R${round(l,2)}\n")
            w=0
            l=0
            if i== 5:
                i=1
                print(f"Você ja ganhou o dia!")
                break
               
        if opt == 0:
            i=1
            d1= s*0.1
            print(f"Você deve usar {d1:.2f}\n")
            bd.write(f"{dft} - Rendimento: {round(rendimento-(s*0.1),2)}\n-------------------------------------------------------\n")
        elif p == 0:
            w += d1*1.92
            l += l - d1
            rendimento += w-d1
            banca += w+l
            bd.write(f"{df} - win: R${round(w,2)}\n")
            bd.write(f"{df} - loss: R${round(l,2)}\n")
            w=0
            l=0
    elif p == 0:
        print("Indo para o próximo loop\n")
    else:
        print("opção invalida\n")

bd.write(f"{dft} - Rendimento: {round(rendimento,2)} / Banca: {round((banca+rendimento),2) }\n-------------------------------------------------------\n")
rendimento = 0
banca = 0

# Concluir o desenvolvimento da soma e subtração para o total
# Desenvolver um break pra parar após 3 loss seguidas de diferença entre as wins Ex: 6 wins com 3 loss consecutivas = break