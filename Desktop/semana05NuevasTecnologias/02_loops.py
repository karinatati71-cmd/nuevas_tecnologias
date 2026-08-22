#while/mientras que

#para sumar de 1 en 1
# condicion = 0
# while condicion <=10:#en el while se utiliza el else y en el if en ningun otro
#     print(condicion)
#     condicion+=1
# else:
#     print('salio del bucle')

#es un contador que me llega hasta 6 y cuando llega a 6 toma un break
# contador = 0
# while True:
#     print(contador)
#     contador+=1
#     if contador ==6:
#         break #sale del bucle




#NUMERO PAR
# contador = 0
# while contador < 10:
#     contador+=2
#     if contador % 1== 2:
#         continue
#     print(contador)


# numero = -1
# while numero <0:

#     try:#cuando tenemos un try es para evitar errores y siempre que este el try necesita un except
#     numero=int(input('ingrese un numero positivo'))
#     if numero < 0:
#         print(f'tu numero {numero} no es un numero positivo')

#      except:
#     print('lo que que ingresaste es un numero!')
# print(f'el numero que ingresaste es el {numero} ')
    

#RETO
# contraseña=input("crea una contraseña:")
# while len(contraseña) >= 8:#len es para contar el numero de variables
#     print(f"tu contraseña es valida puedes seguir")
#     break
# if len(contraseña) < 8:
#     print(f"tu contraseña no es valida tiene menos de 8 caracteres")
# else:
#     print("vuelve a intentarlo")



# match / case
# opcion = int(input("elija alguna de las opciones\n1. Saludo\n2. Ayuda\n3. Adios"))
# match opcion:
#     case 1:
#         print("holiii como tas")

#     case 2:
#         print("ayudameeee")


#     case 3:
#         print("saliste del sistema")

#     case _:
#         print("opcion invalida")   

#upper = para pasar todo a mayuscula
# nota = input("ingresa tu nota(A, B, C, D, F,)").upper()
# match nota:
#     case "A":
#         print("APROBASTE FELICITACIONES")

#     case "B":
#         print("Super bien")

#     case "C":
#         print("Puedes mejorar")

#     case "D":
#         print("ojo que vas perdiendo")
#     case "F":
#         print("perdiste")
#     case _:
#         print("no valido")

#reto
# dia = int(input("elige un dia\n0. lunes\n1. martes\n2.  miercoles\n3. jueves\n4. viernes\n5. sabado\n6. domingo\n7."))

# match dia:
#     case 0:
#         print("elegiste el lunes inicio de semana")

#     case 1:
#         print("elegiste martes un buen dia ")

#     case 2:
#         print("elegiste miercoles mitad de semana")

#     case 3:
#         print("elegiste jueves")

#     case 4:
#         print("elegiste viernes")

#     case 5:
#         print("elegiste sabado")

#     case 6:
#         print("elegiste domingo fin de la larga semana ")

#     case _:
#         print("dia invalido")


#reto 2

# operaciones: int(input("cual va a ser tu operacion\n0. suma\n1. resta\n2. division\n3. multiplicacion\n4"))
# match operaciones:
#     case 0:
#         suma1=int(input("pon un valor que quieras sumar"))
#         suma2=int(input("pon un segundo valor"))
#         total=suma1 + suma2
#         print(total)

#     case 1 :
#         resta1=int(input("pon un numero que quieras restar"))
#         resta2=int(input("pon un segundo numero"))
#         total=resta1 - resta2
#         print(total)

#     case 2:
#         division=int(input("pon un numero que quieras dividir"))
#         div2= int(input("pon el segundo nuemro"))
#         total= division + div2
#         print(total)


#ciclo for
# frutas =["manzana" , "pera" , "uva"]#escoger un rango de donde hasta donde 

# for fruta in frutas:
#     print(fruta)

#imprima los numeros desde el 1 hasta el 5; si o si va a ir hasta el 5

# for i in range(1,6):
#     print(i)

#reto3
# suma = 0
# for i in range (1,101):
#     suma += i
   
#     print(f"tu resultado es {suma}")




 










    
    