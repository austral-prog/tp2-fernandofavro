def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    vuelto = money - expense
    print("Vuelto")
    print("")
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    centavos = 0.25 * 100
    print(int(centavos))
change()