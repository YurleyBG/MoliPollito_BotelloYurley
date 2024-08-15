import json

def abrirmenu():
    file=[]
    with open("menu.json", encoding="utf-8") as data:
        file=json.load(data)
        
        return file 
    
def abrirpedidos():
    files=[]
    with open("pedidos.json", encoding="utf-8") as datas:
        files=json.load(datas)
        
        return files
    
def guardarArchivo(midato):
    with open("pagos.json", "w") as file:
        json.dump(midato,file)


def abrirpagos():
    fua=[]
    with open("pagos.json", encoding="utf-8") as dates:
        fua=json.load(dates)
        
        return fua
    
def guardarpagos(miguar):
    with open("pedidos.json", "w") as fil:
        json.dump(miguar,fil)

info=abrirmenu()
def menucomida():
    print("===========MENÚ===============\n"
    "1. Entrada\n"
    "2. Plato fuerte\n"
    "3. Bebidas\n"
    "4. Salir\n"
    "========================================"
    )

def menuopciones():
    print("===========MENÚ===============\n"
    "1. Registros de pedidos\n"
    "2. Editar pedidos\n"
    "3. Registros de pagos\n"
    "4. Consultar pedidos \n"
    "5. Salir\n"
    "========================================"
    )
pago=abrirpagos()   
datoss=abrirpedidos()  
info=abrirmenu()
bool=True
while bool==True:
    menuopciones()
    print("Escoja la opción a la que desea acceder:")
    opc=int(input())
    
    if opc==1:
        print("========REGISTRAR PEDIDOS==========")
        cliente=input("ingrese el nombre: ")
        print("Este es nuestro menú, Elige la opción de la que deseas realizar tu pedido: ")
        kameha=True
        while kameha==True:
            menucomida()
            print("")
            info=abrirmenu()
            print("elige una opción ")
            choose=int(input())
            print("")
            eleccion=True
            while eleccion==True:
                if choose==1:
                    print("======ENTRADA======")
                    for i in info[0]["entrada"]:
                        print("-","nombre:",i["nombre"] ," " "precio:",i["precio"])
                    categoria="entrada"
                    
                    nombre=input("ingrese el nombre del producto:")
                    for a in info[0]["entrada"]:
                        if  a["nombre"]==nombre:
                            precio=a["precio"]
                            break
                    estado=input("ingrese el estado de preparción")
                  
                    if  nombre != a["nombre"]:
                        print("no se encuentra ningun producto")
             
                    print("desea añadir algo más: si(si) no(no)")
                    cho=input()
                    if cho=="si":
                        eleccion=False
                        kameha=True
                        
                    elif cho=="no":
                        print("regresando al menu principal....")
                        eleccion=False
                        kameha=False
                    
            
           
                if choose==2:
                    print("======PLATO FUERTE======")
                    for i in info[0]["plato_fuerte"]:
                        print("-","nombre:",i["nombre"] ," " "precio:",i["precio"])
                    categoria="plato_fuerte"
                    nombre=input("ingrese el nombre del producto:")
                    for a in info[0]["plato_fuerte"]:
                        if  a["nombre"]==nombre:
                            precio=a["precio"]
                            break
                  
                    if  nombre != a["nombre"]:
                        print("no se encuentra ningun producto")
             
                    print("desea añadir algo más: si(si) no(no)")
                    cho=input()
                    if cho=="si":
                        eleccion=False
                        kameha=True
                    elif cho=="no":
                        print("regresando al menu principal....")
                        eleccion=False
                        kameha=False
                            
                if choose==3:
                    print("======BEBIDAS======")
                    for i in info[0]["bebida"]:
                        print("-","nombre:",i["nombre"] ," " "precio:",i["precio"])
                    categoria="bebida"
                    nombre=input("ingrese el nombre del producto:")
                    cantidad=input("cual es la cantidad adquirida: ")
                    for a in info[0]["bebida"]:
                         if  a["nombre"]==nombre:
                            precio=a["precio"]
                            print(precio)
                            break
   
                    if  nombre != a["nombre"]:
                        print("no se encuentra ningun producto")
             
                    print("desea añadir algo más: si(si) no(no)")
                    cho=input()
                    if cho=="si":
                        eleccion=False
                        kameha=True
                    elif cho=="no":
                        print("regresando al menu principal....")
                        eleccion=False
                        kameha=False
                        
                if choose==4:
                    print("")
                    print("regresando al menú principal...")
                    eleccion=False
                    kameha=False
            datoss[0]["pedidos"].append({"cliente":cliente,"items":[{"categoria": categoria,"nombre":nombre,"precio":precio  }],"estado":estado})
            guardarArchivo(datoss)         
            print("Su registro a sido exitoso!")
    if opc==2:
        print("========EDITAR PEDIDOS===========")
        print("")
        print("Escribe el nombre de la persona de la cual estas buscando los pedidos:")
        pcliente=input()
        for i in datoss[0][ "pedidos"]:
            if pcliente==i["cliente"]:
                for a in i["items"]:
                    print("")
                    print("::::::::Registros::::::::::")
                    print("Cliente:",i["cliente"])
                    print("Categoria:", a["categoria"])
                    print("Nombre:",a["nombre"])
                    print("Precio:",a["precio"])
                    print("Estado:", i["estado"])  
                    print("::::::::::::::::::::::::::::")
                    print("")
                    pedido=False  
                    bool=True
        if pcliente!=i["cliente"]:  
            print("")
            print("No se encuentra registro de algun cliente con este nombre ")
            print("Intentalo de nuevo...")
            print("")
            pedido=True           
    if opc==3:
        print("========REGISTRAR PAGO===========")
        for i in pago[0]["pagos"]:
            cliente=input("ingrese el nombre del cliente: ")
        

    if opc==4:
           
           pedido=True
           while pedido==True:
                print("========CONSULTAR PEDIDOS===========")
                print("Deseas ver todo los pedidos (all) o buscar alguno en especifico(other)")
                ingre=input()
                if ingre=="all":
                    print("--------TODO LOS REGISTROS------------")
                    for i in datoss[0][ "pedidos"]:
                        for a in i["items"]:
                            print("")
                            print("::::::::Registros::::::::::")
                            print("Cliente:",i["cliente"])
                            print("Categoria:", a["categoria"])
                            print("Nombre:",a["nombre"])
                            print("Precio:",a["precio"])
                            print("Estado:", i["estado"])  
                            print("::::::::::::::::::::::::::::")
                            print("")
                if ingre=="other":
                    print("")
                    print("Escribe el nombre de la persona de la cual estas buscando los pedidos:")
                    pcliente=input()
                    for i in datoss[0][ "pedidos"]:
                        if pcliente==i["cliente"]:
                            for a in i["items"]:
                                print("")
                                print("::::::::Registros::::::::::")
                                print("Cliente:",i["cliente"])
                                print("Categoria:", a["categoria"])
                                print("Nombre:",a["nombre"])
                                print("Precio:",a["precio"])
                                print("Estado:", i["estado"])  
                                print("::::::::::::::::::::::::::::")
                                print("")
                                pedido=False  
                                bool=True
                    if pcliente!=i["cliente"]:  
                        print("")
                        print("No se encuentra registro de algun cliente con este nombre ")
                        print("Intentalo de nuevo...")
                        print("")
                        pedido=True           
    if opc==5:
        print("Tü has finalizado el programa")
        print("Cerrando programa...")
        bool=False
       
                
       
        