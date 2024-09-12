nota_1 = float(input("Ingresa la nota 1: "))
nota_2 = float(input("Ingresa la nota 2: "))
nota_3 = float(input("Ingresa la nota 3: "))
nota_4 = float(input("Ingresa la nota 4: "))

suma_notas = nota_1 + nota_2 + nota_3 + nota_4

promedio = suma_notas / 4 


if promedio > 3.5:
    print("Aprobado")
else:
    print("No pasa")