# #los set
# #no tiene orden
# #nO permite repetidos
# #si se puede modificar
# numeros = {1,2,3,4,5,6}
# print(numeros)
# print(type(numeros))
# #agregar unnnuevo dato
# print((f"este es el set original {numeros}"))
# numeros.add(7)#no se le puede poner el append porque no tiene unnorden el append agrega hasta el final
# print(f"este es el set original con un dato mas{numeros}")

# #agregar varias cosas al mismo tiempo con el update()
# numeros.update([8,9,10])
# print(numeros)

# #eliminar un dato
# numeros.remove(10)
# print(numeros)

# #tomar unelemento aleatorio pop()
# lo_eliminado = numeros.pop()#para poder ver los datos eliminados ponemos una variable nueva para que nos muestre que elimino 
# print(lo_eliminado)

# print(numeros)


# #verificar si algo esta en el set
# print("esta el 2 en la lista ? " , 2 in numeros)

# #operaciones especiales con sets (pleca) para unir un set 


# b={1,2,3}
# c={3,4,5,6}

# print(b|c)

# #interseccion lo que tienen en comun
# print( c & b)
# #lo que no tienen en comun

# print(b - c) 
# print( c - b)

# #convertir una lista a set y de set a lista . para eliminar lo srepetidos

# lista = [1,1,1,2,3,4,4,5,6,6]
# no_repetidos=list(set(lista))
# print(type(no_repetidos))
# print(no_repetidos)


# #DICCIONARIOS
# #guarda informacion clave - valor

# personas={
#     "nombre" : "Maria",
#     "vive" : "Mexico",
#     "edad" : 28
    
   
# }
# #se llaman los datos
# print(personas["nombre"])
# print(personas["edad"])
# print(personas["vive"])

# #cambiar un valor
# personas["nombre"] = "Jose"

# #agregar un valor 
# personas["trabajo"] = "veterinario"

# print(personas)

# #eliminar un dato
# del personas["edad"]

# #claves traer los valores de las claver
# for contraseña in personas:
#     print(contraseña)

# #traer los valores
# for valor in personas.values():
#     print(valor)


# #como traer la clave y el valor 
# for valor in personas.items():
#     print(valor)

# #para ver si esta en la lista 
# for "edad" in personas:
#     print("existe")








##retos
# # el diccionario
# libro = {
#     "titulo": "El principito",
#     "autor": " Antoine de Saint-Exupéry",
#     "año": 1943,
#     "precio": 10500
# }
 

# print("--- Datos del libro ---")
# for clave, valor in libro.items():
#     print(clave, ":", valor)
 

# libro["precio"] = 10500
 

# libro["editorial"] = "Antoine de Saint-Exupéry"
 

# del libro["año"]
 
# print("\n--- Diccionario modificado ---")
# print(libro)

# clave_buscada = input("\n¿Qué dato quieres buscar? (ejemplo: titulo, autor, precio): ")
 
# if clave_buscada in libro:
#     print("¡Sí existe! :", libro[clave_buscada])
# else:
#     print("Lo siento,  no existe en el libro.")

# print(libro)
   
   
## con sets
 

numeros = set([1, 2, 2, 3, 4, 4, 5])
 
print("--- Eliminación de duplicados ---")
print("El set quedó así (sin repetidos):", numeros)
 
numeros.add(6)
numeros.add(7)
print("Después de agregar 6 y 7:", numeros)
 

numeros.remove(3)
print("Después de quitar el 3:", numeros)
 

if 5 in numeros:
    print("El 5 sí está en el set.")
else:
    print("El 5 no está.")

grupo_a = {1, 2, 3, 4}
grupo_b = {3, 4, 5, 6}
 
print("\n--- Operaciones ---")
print("Grupo A:", grupo_a)
print("Grupo B:", grupo_b)
 
print("Unión (A | B):", grupo_a | grupo_b)
 

print("Intersección (A & B):", grupo_a & grupo_b)
 

print("Diferencia (A - B):", grupo_a - grupo_b)


