#Ingresar el sueldo de una persona, si supera los 80000000 millores mostrar un
#mensaje en pantalla indicando que debe abonar IRP.
#sino mostrar el mensaje la persona No debe abonar impuestos
sueldo=(int(input("ingrese cual es su sueldo : ")))
sueldo_anual=sueldo*12
IRP=80000000
if sueldo_anual > IRP:
    print("debes de abonar IRP")
else :
    print("no debes de abonar impuestos")