
def euro_dolar(euro):
    global cambio
    dolar = euro * cambio
    return dolar
def dolar_euro(dolar):
    global cambio
    euro = dolar / cambio
    return euro
def guardar_dato():
    dato = input("Dime cual es el tipo de cambio ->")  

    try:
        with open('dato_cambio.txt','w') as f:
            f.write(str(dato))
            print("Dato guardado")
    except IOError:
        print("No se pudo escribir en el fichero")
    
def leer_dato():
    dato = 1.09 # 1 euro = 1.09 dolares
    try:
        with open('dato_cambio.txt','r') as f:
            dato = float(f.read())
            return dato
    except FileNotFoundError:
        print("Error: fichero no encontrado")
def menu():
    print('1.Cambiar a dolares\n2.Cambiar a euros\n3.Guardar dato\n4.Salir')
    opcion = int(input("-> "))
    return opcion
def main():
    global cambio
    cambio = leer_dato()
    while True:
        opcion=menu()
        if opcion == 1:
            importe = float(input("Dime los euros a cambiar "))
            dolares = euro_dolar(importe)
            print(f"El cambio en dolares es de {dolares} dolares ")
        elif opcion== 2:
            importe = float(input("Dime los dolares a cambiar "))
            euros = dolar_euro(importe)
            print(f"El cambio en euros es de {euros} euros")
        elif opcion==3:
            guardar_dato()
            
            cambio = leer_dato()
        elif opcion==4:
            print("Hasta pronto!!!")
            break
        else:
            print("Selecciona opcion correcta")
    
if __name__=='__main__':
    main()
           
