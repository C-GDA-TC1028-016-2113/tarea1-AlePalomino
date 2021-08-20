def main():
    #escribe tu código abajo de esta línea
    peso_inicial = int(input("Dame el peso inicial: "))
    peso_final = int(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    dif = (peso_inicial - peso_final) / meses
    print ("Lo que debes bajar por mes es:", dif)




if __name__ == '__main__':
    main()
