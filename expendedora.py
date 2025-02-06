import os

nombresProductos = ["Agua","Refresco","Zumo"]
preciosProductos = [0.50,0.75,0.95]
reservaMonedas = [20,20,20,20,20,20]
valoresMonedas = [2,1,0.50,0.20,0.10,0.05]
dinero = 0
os.system('clear')

def entrada(reserva, valores, dinero):
    moneda = 0
    while moneda != 7:
        os.system('clear')
        cont = 0
        textoMenu = ""
        for valor in valores:
            textoMenu += f"{cont+1} - Introducir {valor} € \n"
            cont += 1
        textoMenu += f"{cont+1} - Salir"

        print(textoMenu)
        print("Dinero =",dinero)
        moneda = int(input(">> "))

        if moneda != 7:
            reserva[moneda - 1] += 1
            dinero = round(dinero + valores[moneda - 1],2)
    os.system('clear') 
    return(dinero)

def menu(nombres, precios, dinero, reserva, valores):
    cont = 0
    textoMenu = ""
    
    for nombre in nombres:
        textoMenu += f"{cont+1} - {nombre} : {precios[cont]} \n"
        cont += 1
    textoMenu += f"{cont+1} - Introducir monedas \n"
    textoMenu += f"{cont+2} - Salir"
    
    print(textoMenu)
    print(f"Dinero = {dinero}")
    num = int(input(">> "))

    if num == 4:
        dinero = entrada(reservaMonedas, valoresMonedas, dinero)
    elif num == 5:
        print("")
        print(reserva)
        print(valores)
        quit()
    elif (dinero >= precios[num-1] ):
        dinero = round(dinero-precios[num-1],2)
        cambio(reservaMonedas, valoresMonedas, dinero)
    elif (dinero < precios[num-1] ):
        os.system('clear')
        print("Dinero insuficiente \n")
    else:
        quit()
    return(dinero)

def cambio(reserva,valores,vueltas):
    cambio = []
    os.system('clear')

    for i in range(len(valoresMonedas)):
        while(valores[i] <= vueltas and reserva[i] > 0):
            reserva[i] -= 1
            vueltas = round(vueltas - valores[i], 2)
            cambio.append(valores[i])
    print(f"El cambio es {cambio} \n")

while True:
    dinero = menu(nombresProductos, preciosProductos, dinero, reservaMonedas, valoresMonedas)

print("")
print(valoresMonedas)
print(reservaMonedas)