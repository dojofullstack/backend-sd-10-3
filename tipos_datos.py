
# Tipos de Datos

"""
    - String
    - Number
    - Boolean
    - Dict
    - Listas
    - Set
    - Tuples
"""

# String

email = "pedro@gmail.com"
print(email)

# print( type(email))
# print(str(123))

# print(dir(email))


print( email.replace("gmail", "hotmail") )

print(email.title())

print(email.find("@"))

print(email.count("@"))

lista = email.split("@")
# print(lista)

print("@".join(lista))


# Number

precio = 123.5
puntaje = 10

print(type(precio))
print(type(puntaje))


precio += 5
precio -= 2
precio *= 3
precio /= 2

precio += 1

# float()
# int()

# Bool

isMember = True
isAdmin = False

print(type(isMember))
print(type(isAdmin))

# bool()


# dict

usuario = {
    "name": "pedro",
    "edad": 12,
    "isAdmin": True,
    "preferencias": ["color verde", "tema light"]
}

print(type(usuario))

# para crear y actualizar
usuario["email"] = "pedro@gmail.com"

print(usuario)

# print(usuario["plan"])

print(usuario.get("plan", "FREE" ))


# print(usuario.items())

print(usuario.keys())
print(usuario.values())

#usuario.pop("edad")
#del usuario["email"]

print(usuario)




# List

stack = ["python", "javascript", "perl", "golang"]

print(stack)

stack.append("django")

stack.remove("golang")




stack.extend(["react", "node"])


print(type(stack))

# stack.insert(0, "flutter")

#list()

print(stack)


# tuplas
frutas = ("fresas", "naranjas", "uvas")
print( type(frutas) )

