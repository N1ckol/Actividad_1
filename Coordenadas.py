
def menu():
    print("1. DD a DMS ")
    print("2. DMS a DD")
    
def Conversion(numero):
   si_positivo = numero >= 0
   numero = abs(numero)
   minutes,seconds = divmod(numero*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if si_positivo else -degrees
   return (degrees,minutes,seconds);

def dms2dd(tup1):
    dd = float(tup1[0]) + float(tup1[1])/60 + float(tup1[2])/(60*60);
    return dd;

print("Seleccione el tipo de conversión que desea realizar: ");

menu()

option = int(input("Seleccione el numero: "))
 
while option != 0:
    if option == 1:
        numero = float(input("Ingrese el valor de la Latitud en DD: "))
        print("El valor de la latitud es:");
        print(Conversion(numero));
    elif option == 2:
        dd = float(input("Ingrese el valor de la Latitud en DD: "))
        print("El valor de la latitud es:");
        print(dms2dd(dd));
    else:
        print("No existe esa opcion.")

    menu()      

    option = int(input("Introduzca su opcion: "))
 
