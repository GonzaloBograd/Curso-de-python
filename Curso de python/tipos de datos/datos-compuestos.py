# Creando una lista (se puede modificar)
lista = ["Gonzalo Bograd", "Soy Gonazalo", True, 1.80]  #Lista (list)  #elemento "Gonzalo Bograd" es 0 

# Creanndo una tupla (no se puede modificar)
tupla = ("Gonzalo Bograd", "Soy Gonazalo", True, 1.80)  #Tupla (tuple)  #elemento "Gonzalo Bograd" es 0

# Esto es valido 
lista [3] = "Maquinola"

# Esto no es valido 
#tupla [3] = "Maquinola"

# Creando un conjunto (set) (no accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Gonzalo Bograd", "Soy Gonazalo", True, 1.80}  #Conjunto (set)  #elemento "Gonzalo Bograd" no tiene indice

# print(conjunto[3]) -> no puede acceder por elemento

#crando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    "nombre": "Gonzalo Bograd",
    "profesion": "Soy Gonzalo",
    "soltero": True,
    "altura": 1.80,
}

print(diccionario["profesion"])