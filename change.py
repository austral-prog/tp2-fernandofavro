def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{int(money - expense)}\nCentavos:\n{int((money - expense) * 100 % 100)}")
change()