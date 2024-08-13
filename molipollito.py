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
    with open("info.json", "w") as file:#esto es para guardar info en el json de info
        json.dump(midato,file)

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
    "4. Consulta de pedidos \n"
    "5. Salir\n"
    "========================================"
    )
    
    
info=abrirmenu()
bool=True
while bool==True:
    menuopciones()
    print("Escoja la opción a la que desea acceder:")
    opc=int(input())
    
    if opc==1:
        print("========REGISTRAR PEDIDOS==========")
        
        nombre=input("ingrese el nombre: ")
        print("Este es nuestro menú, Elige la opción de la que deseas realizar tu pedido: ")
        menucomida()
        kameha=True
        while kameha==True:
            print("")
            info=abrirmenu()
            print("elige una opción ")
            choose=int(input())
            print("")
            if choose==1:
                print("======ENTRADA======")
                for i in info[0]["entrada"]:
                    print("-","nombre:",i["nombre"] ," " "precio:",i["precio"])
                categoria="entrada"
                nombre=input("ingrese el nombre del producto:")
                for a in info[2]["entrada"]:
                    if  a["nombre"]==nombre:
                        precio= a["precio"]
                        print(precio)
                        break
                    elif  nombre != a["nombre"]:
                        print("no se encuentra ningun producto")
                        break
            if choose==2:
                print("======PLATO FUERTE======")
                for i in info[0]["plato_fuerte"]:
                    print("-","nombre:",i["nombre"] ," " "precio:",i["precio"])
                categoria="plato_fuerte"
                nombre=input("ingrese el nombre del producto:")
                for a in info[0]["plato_fuerte"]:
                    if  a["nombre"]==nombre:
                        precio= a["precio"]
                        print(precio)
                        break
                    elif  nombre != a["nombre"]:
                        print("no se encuentra ningun producto")
                        break
            if choose==3:
                print("======BEBIDAS======")
                for i in info[0]["bebida"]:
                    print("-","nombre:",i["nombre"] ," " "precio:",i["precio"])
                categoria="bebida"
                nombre=input("ingrese el nombre del producto:")
                for a in info[0]["bebida"]:
                    if  a["nombre"]==nombre:
                        precio= a["precio"]
                        print(precio)
                        break
                    elif  nombre != a["nombre"]:
                        print("no se encuentra ningun producto")
                        break
            if choose==4:
                print("")
                print("regresando al menú principal...")
                
                kameha=False
                
       
        