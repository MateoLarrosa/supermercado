from codigo.supermercado import Cliente

#funcion para pedir los datos al cliente
def obtener_datos_cliente():
    print('Ingrese los siguientes datos para poder comenzar con la compra:')
    nombre = input('Ingrese su nombre: ')
    while True:
        try:
            dni = int(input('Ingrese su dni: '))
            break
        except:
            print('El dni solo puede contener numeros')
    mail = input('Ingrese su mail: ')
    while True:
        try:
            dinero = int(input('Ingrese la cant de dinero que tiene: $'))
            break
        except:
            print('Tiene que ingresar el monto en numeros')

    cliente = Cliente(nombre, dni, mail, dinero)
    return cliente

#Creando al cliente
cliente1 = obtener_datos_cliente()

#menu para que el cliente pueda acceder a los distintos metodos
while True:
    print("""
    que desea hacer?
    1- ver catalogo
    2- comprar
    3- Mis datos
    4- salir
          """)
    decision = input('Ingrese aqui la opcion: ')
    
    if decision == '1':
        cliente1.catalogo()
        continue
    elif decision == '2':
        cliente1.comprar()
        if cliente1.finalizar_compra() != False:
            continue
    elif decision == '3':
        cliente1_str = cliente1.__str__()
        print(cliente1)
        continue
    elif decision == '4':
        break
    else:
        print('La opcion que elijio no es valida, intente nuevamente')
        continue