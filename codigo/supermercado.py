class Cliente:
    #metodo constructor de la clase Cliente
    def __init__(self,nombre,dni,mail,dinero):
        self.nombre = nombre
        self.dni = dni
        self.mail = mail
        self.dinero = dinero
        self.carrito = {}
        self.productos_agregados = {}


    #metodo para mostrar el catalogo
    def catalogo(self):
        print("""
        BIENVENIDO A JUMBO
    
               CATALOGO
        ====================
        
            COMIDAS:
            
        1- ARROZ $300
        2- MILANESAS $220
        3- YOGURT $400
        
        ELECTRODOMESTICOS:
        
        1- TABLET $1000
        2- CELULAR $2500
        3- PS4 $4000
        
            ALCOHOL:
        
        1- VODKA $500
        2- CHAPAGNE $700
        3-VINO $450
        
        ====================
              """)


    # Metodo para que el cliente pueda realizar la compra en el "supermercado"
    def comprar(self):
        # dicc del catalogo donde se buscarian los productos que el cliente quiere comprar
        catalogo = {
            'arroz' : 300,
            'milanesas' : 220,
            'yogurt' : 400,
            'tablet' : 1000,
            'celular' : 2500,
            'ps4' : 4000,
            'vodka' : 500,
            'champagne' : 700,
            'vino' : 450
            }
        while True:
            
            seguir_comprando = input('Escriba "esc" si quiere dejar de comprar.para seguir con la compra toque enter: ')
            if seguir_comprando.lower() == 'esc':
                # se termina el bucle y se lo lleva al cliente a pagar los productos
                break
            else:
                # Distinas condiciones segun lo que ingrese el cliente para llevarlo a las secciones del "supermercado"
                self.Catalogo()
                seccion = input('Ingrese aqui la seccion: ')
                
                # si es menor de edad no puede ingresar a la seccion de alcohol.
                # se comprueba por los dni mayores a 46.000.000 que serian los que todavia no son mayores de edad
                if seccion.lower() == 'alcohol' and self.dni > 46000000:
                    print('Usted no puede acceder a la parte de alcohol ya que es menor de edad')
                    continue
                # dni menor a 46.000.000 asi que puede acceder
                elif seccion.lower() == 'alcohol' and self.dni < 46000000:
                    print("""
                    ===============
                    ALCOHOL:
                    
                    1- VODKA $500
                    2- CHAMPAGNE $700
                    3-VINO $450
                    ===============""")
                    while True:
                        producto = input('Ingrese el producto que quiere comprar,si quiere salir de esta seccion escriba "esc": ')
                        if producto.lower() == 'esc':
                            break
                        else:
                            # Si el producto esta en el catalogo lo agrega al carrito
                            if producto in catalogo:
                                if producto in self.carrito:
                                    #en el dicc productos_agregados se lleva el conteo de las uds por producto que esta llevando
                                    if producto in self.productos_agregados:
                                        self.productos_agregados[producto] += 1
                                        print(f'Se agrego {producto} al carrito!!')
                                    else:
                                        self.productos_agregados[producto] = 2
                                        print(f'Se agrego {producto} al carrito!!')
                                else:
                                    self.carrito[producto] = catalogo[producto]
                                    print(f'Se agrego {producto} al carrito!!')
                                    continue
                            # Si no se encuentra en el catalogo se le informa al cliente
                            else:
                                print(f'{producto} no se encuentra en nuestra seccion de {seccion}, ingrese uno disponible')
                                continue
                elif seccion.lower() == 'electrodomesticos':
                    print("""
                    ===============
                    ELECTRODOMESTICOS:
                    
                    TABLET $1000
                    CELULAR $2500
                    PS4 $4000
                    ===============""")
                    while True:
                        producto = input('Ingrese el producto que quiere comprar,si quiere salir de esta seccion escriba "esc": ')
                        if producto.lower() == 'esc':
                            break
                        else:
                            # Si el producto esta en el catalogo lo agrega al carrito
                            if producto in catalogo:
                                if producto in self.carrito:
                                    #en el dicc productos_agregados se lleva el conteo de las uds por producto que esta llevando
                                    if producto in self.productos_agregados:
                                        self.productos_agregados[producto] += 1
                                        print(f'Se agrego {producto} al carrito!!')
                                    else:
                                        self.productos_agregados[producto] = 2
                                        print(f'Se agrego {producto} al carrito!!')
                                else:
                                    self.carrito[producto] = catalogo[producto]
                                    print(f'Se agrego {producto} al carrito!!')
                                    continue
                            # Si no se encuentra en el catalogo se le informa al cliente
                            else:
                                print(f'{producto} no se encuentra en nuestra seccion de {seccion}, ingrese uno disponible')
                                continue
                
                elif seccion.lower() == 'comidas':
                    print("""
                    ===============
                    COMIDA:
    
                    ARROZ $300
                    MILANESAS $220
                    YOGURT $400
                    ===============""")
                    while True:
                        producto = input('Ingrese el producto que quiere comprar,si quiere salir de esta seccion escriba "esc": ')
                        if producto.lower() == 'esc':
                            break
                        else:
                            # Si el producto esta en el catalogo lo agrega al carrito
                            if producto in catalogo:
                                if producto in self.carrito:
                                    #en el dicc productos_agregados se lleva el conteo de las uds por producto que esta llevando
                                    if producto in self.productos_agregados:
                                        self.productos_agregados[producto] += 1
                                        print(f'Se agrego {producto} al carrito!!')
                                    else:
                                        self.productos_agregados[producto] = 2
                                        print(f'Se agrego {producto} al carrito!!')
                                else:
                                    self.carrito[producto] = catalogo[producto]
                                    print(f'Se agrego {producto} al carrito!!')
                                    continue
                            # Si no se encuentra en el catalogo se le informa al cliente
                            else:
                                print(f'{producto} no se encuentra en nuestra seccion de {seccion}, ingrese uno disponible')
                                continue
                #Si la seccion que ingreso no se encuentra en nuestro catalogo, se le informa al cliente
                else:
                    print('La seccion que ingreso no existe en nuestro catalogo, intente nuevamente')
                    continue


    def finalizar_compra(self):
        # Se agrega al value(precio) de cada key(producto)
        # el valor total que tienen que pagar segun la cant de uds que compraron de ese producto
        for key_carrito,value_carrito in self.carrito.items():
            for key_agregados,value_agregados in self.productos_agregados.items():
                if key_carrito == key_agregados:
                    self.carrito[key_carrito] = value_carrito * value_agregados

        #se calcula el valor total de la compra
        total_de_compra = sum(self.carrito.values())
        
        #Si el total de la compra es superior al dinero que dijo que tenia se le informa que no puede hacer la compra
        if total_de_compra >= self.dinero and len(self.carrito) > 0  :
            print('Productos comprados:')
            for keys,value in self.carrito.items():
                print(f'{keys} : ${value}')
            print('No tiene el dinero suficiente para comprar todo lo que agrego al carrito,vuelva y haga la compra con el dinero justo')
            print(f'total de la compra: ${total_de_compra}')
            print(f'dinero disponible: ${self.dinero}')
            return True
        
        # si el dinero le da para hacer la compra cumple la condicion y se le muestran detalles de la misma
        elif total_de_compra <= self.dinero and len(self.carrito) > 0 :
            print('Productos comprados:')
            for keys,value in self.carrito.items():
                print(f'{keys} x{self.productos_agregados[keys]} uds : ${value}')
            vuelto =self.dinero - total_de_compra
            print(f'\ntotal de la compra: ${total_de_compra}\ndinero disponible: ${self.dinero}\nGracias {self.nombre} por confiar en nosotros, su vuelto es de ${vuelto}\nSe le mando un mail a {self.mail} con el resumen de la compra\nHasta pronto!!!!')
            self.dinero = vuelto
        # Si entro a comprar pero decidio irse con el carrito vacio, se le informa y se retira tranquilamente
        else:
            print('Este mensaje es solo para avisarle que usted no compro nada, hasta pronto!!!')
            return True
    # Metodo __str__ que devuelve en forma de texto los datos del cliente.


    def __str__(self):
        return f'Nombre: {self.nombre}\nDNI: {self.dni}\nMail: {self.mail}\nDinero: ${self.dinero}\nCarrito: {self.carrito}'