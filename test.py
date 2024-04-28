from datetime import datetime
from datetime import date

data = datetime.now()
df=data.strftime('%d/%m/%Y %H:%M')
dtf=data.strftime('%d/%m/%Y')

loop=0
e=0 #entrada
vf=0 #valor fixo
i=1
w=0
l=0
r=0
b=0
x=0
bd=open('teste.txt','a')

s=10

bd.write(f"{dtf} - Banca Inicial: {s}\n")
while True:
    loop += 1
    if loop > 10:
        break
    print(f"{loop}° loop")
    0
    if s<1:
        print("valor insuficiente")
        break
    else:
        e=s*0.1
        r+=e
        print(f"Você deve usar {e:.2f}")
        bd.write(f"\n{df} Entrada de: R${e:.2f}\n")
        opt = int(input("Você ganhou? Digite '1' para sim ou '0' para não: "))

        while opt == 1:
            d=d*1.5
            i+=1
            print(f"Você deve usar {e:.2f} para a {i}° vez\n")
            opt = int(input("Você ganhou? Digite '1' para sim ou '0' para não: "))
            
            if opt == 1:
                b+=e*1.92
                bd.write(f"{df} - win: R${r:.2f}\n")
            elif opt == 0:
                
                bd.write(f"{df} - loss: R${l:.2f}\n")
                
                break
            
            if i==5:
                i=1
                print(f"Você ja ganhou o dia!")
                x=0
                break
        if opt==0:
            
            bd.write(f"{df} - loss: R${l:.2f}\n")
            l=0
            x+=1
            i=1
            d=s*0.1
            print(f"Você deve usar: R${e:.2f}\n")
            bd.write(f"{dtf} - Rendimento: {r:.2f}\n-------------------------------------------------------\n")
        

bd.write(f"\n{dtf} - Rendimento: R${r:.2f} / Banca: R${(b):.2f}\n-------------------------------------------------------\n")
bd.close()
