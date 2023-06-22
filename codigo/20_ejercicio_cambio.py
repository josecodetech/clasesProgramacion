cambio = 1.09 # 1 euro = 1.09 dolares
def euro_dolar(euro):
    dolar = euro * cambio
    return dolar
def dolar_euro(dolar):
    euro = dolar / cambio
    return euro
def menu():
    print('1.Cambiar a dolares\n2.Cambiar a euros\n3.Salir')
    opcion = int(input("-> "))
    return opcion
def main():
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
            print("Hasta pronto!!!")
            break
        else:
            print("Selecciona opcion correcta")
    #pass
if __name__=='__main__':
    main()
           
