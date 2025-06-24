def menu():
    print("**MENU PRINCIPAL**")
    print("1_ Ingresar numero")
    print("2_ Mostrar mayor")
    print("3_ Mostrar promedio")
    print("4_ Terminar programa")
def principal():
    numeros = []
    suma_numeros = 0
    cantidad_numero = 0
    while True:
        menu()
        opcion = input("Elija alguna opcion: ")
        if opcion == "1":
            while True:

             try:
              entrada = input("ingrese un numero entre 0 y 100: ")
              numero = int(entrada)
              if 0 <= numero <= 100:
               numeros.append(numero)
               suma_numeros += numero
               cantidad_numero += 1
               print("Se ha ingresado el numero")
               break
              else:
                print("opcion no validada intente de nuevo")
             except ValueError:
              print("Debes ingresar una opcion valida")
        elif opcion == "2":
           if numeros:
              print(f"su numero mayor hasta el momento es: {max(numeros)}")
           else:
              print("No a ingresado un numero")
        elif opcion == "3":
           if numeros:
              promedio = suma_numeros / cantidad_numero
              print("El promedio de los numeros ingresados es: ", promedio)
           else:
              print("No se han ingresado numeros")
        elif opcion == "4":
           print("Fin Adios")
           break
        else:
         print("Ingrese una opcion valida")
principal()