#condicionales
#if/elif/else
#mi_variable = False #como es false no entra deltro del if,si es true apareceria dentro del if
#if mi_variable:
#    print("se esta ejecutando dentro del if")

#print('esta fuera del if')


# como se evaluan las condiciones
#mi_variable = 10 #si entra porque es un valor
#if mi_variable > 10:
   # print("se esta ejecutando dentro del if")

#print('esta fuera del if')

#que el usuario ingrese el valor

#mi_variable = int(input("ingrese el valor"))#el input se uiliza para que el usuario ingrese un valor 
#if mi_variable > 10:
 #   print("se esta ejecutando dentro del if")

#print('esta fuera del if')


#si se cumple una condicion se entra en la primera si no pues a la egunda

# mi_variable = int(input("ingrese el valor"))
# if mi_variable > 10:
#     print("se esta ejecutando dentro del if")
# elif mi_variable == 10:
#     print(f'El valor de {mi_variable}cumple la condicion parar entrara a el if')#este funciona como el simbolo de $
# else:
#     print("Ejecutando desde el else")

# print('esta fuera del if')


#RETO
#por consola pida la edad de una persona
edad_persona = int(input("cual es tu edad?"))

cedula = input("tienes cedula si/no")

if edad_persona >= 18  and cedula == "si":
    print("Puedes ingesar")

else:
    
    print(f'no puedes ingresar porq tu edad {edad_persona} o {cedula} no es compatible para el ingreso')








