def menu():
    print("")
    print(".-.-MENU ACME.-.-")
    print("")
    print("1.-Agregar plan")
    print("2.-Listar planes")
    print("3.Eliminar plan por ID-")
    print("4.-Generar BBDD")
    print("5.-cargar BBDD")
    print("6.-Estadísticas")
    print("0.- Salir")
    print("")

def validar():
    porcentaje=int(input("Ingrese porcentaje de efectividad:\n"))
    while porcentaje<0 or porcentaje>100:
        print("El porcentaje debe estar entre 0 y 100")
        porcentaje=int(input("Reingrese porcentaje de efectividad:\n"))
        
def cat_interna():
    if porcentaje>=0 and porcentaje<=25:
        categoria="Chiste"
    elif porcentaje>=26 and porcentaje<=50:
        categoria="Anécdota"
    elif porcentaje>=51 and porcentaje<=75:
        categoria="Peligro"
    elif porcentaje>=76 and porcentaje<=99:
        categoria="Atención"
    elif porcentaje==100:
        categoria="Esclavitud"

    return categoria

        
        
def confirmar(res):
    if res=="si" or res=="s":
        estado=True
    else:
        estado=False
    return estado

def pep():
    acu=0
    for x in lista:
        acu=x[2]+acu
    cantidad=len(lista)
    promedio=acu/cantidad
    print("Porcentaje de efectividad promedio : ",promedio)

def p_masalto():
    total=0
    myr_cant=0
    for x in lista:
        porcentaje=int(x[2])
        total=total+porcentaje
        if porcentaje>myr_cant:
            myr_cant=porcentaje
        print("Valor del porcentaje de efectividad más alto : ",myr_cant)

import csv
lista=[]

while True:
    menu()
    op=int(input("Ingrese una opción : \n"))
    if op==1:
        print("")
        ide=input("Ingrese n°de plan:\n")
        nombre=input("Ingrese nombre de plan:\n")
        
        validar()
        cat_interna()
        listaplan=[ide,nombre,porcentaje,categoria]
        lista.append(listaplan)
        print("")
        print("Plan agregado correctamente")
        print("")
        
        
        
    elif op==2:
        print("")
        print(".-.-LISTAR PLANES.-.-.")
        for plan in lista:
            print("ID : ",plan[0], "Nombre : ",plan[1], "Porcentaje efectividad", plan[2], "Categoría interna : ", plan[3])
    elif op==3:
        encontrado=False
        print("")
        (".-.-Eliminar plan por ID.-.-")
        ide=input("Ingrese ID del plan : \n")
        for plan in lista:
            if ide==plan[0]:
                print("Plan encontrado")
                print("Datos de plan : \n")
                print("ID : ",plan[0], "Nombre : ",plan[1], "Porcentaje efectividad", plan[2], "Categoría interna : ", plan[3])
                encontrado=True
                respuesta=input("¿Está seguro que desea eliminar este plan?(si/no):").lower()
                resultado=confirmar(respuesta)
                if resultado:
                    lista.remove(plan)
                    print("Plan eliminado correctamente")
                else:
                    print("Eliminación cancelada")

            if encontrado==False:
                print("Plan no existe")
                
                    
                
                
    elif op==4:
        print("")
        print(".-.-Generar BBDD.-.-")
        with open ('planes.csv','w',newline='') as planes:
            escritor_csv=csv.writer(planes)
            escritor_csv.writerow(['ID','Nombre','P. efectividad','Cat. Interna'])
            escritor_csv.writerows(lista)
            print("Archivo generado correctamente")
            
    elif op==5:
        print("")
        lista.clear()
        with open ('planes.csv','r',newline='') as planes:
            lector_csv=csv.reader(planes)
            for x in lector_csv:
                lista.append(x)
        lista.pop(0)

        for x in lista:
            print("ID : ",x[0], "Nombre : ",x[1], "Porcentaje efectividad", x[2], "Categoría interna : ", x[3])
            
        
    elif op==6:
        print("")
        print(".-.-Estadísticas.-.-")
        pep()
        p_masalto()
    elif op==0:
        print("Adiósss")
        break
    else:
        print("Ingrese una opción válida")

# 
