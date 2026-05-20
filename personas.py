personas = [{
    "nombre": "carlos",
    "edad": 30,
    "ciudad": "Colombia"
}, {
    "nombre": "camilo",
    "edad": 30,
    "ciudad": "Colombia"
}]

usuario = { "nombre": "Juan", "edad": "30", "ciudad": "Colombia" }

print(usuario["nombre"])

usuario["edad"] = 30

usuario["profesion"] = "ingeniero"

del usuario["ciudad"]

email = usuario.get("email", "No se encontró el email")

usuario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": []
}

usuario["ciudad"].append("colombia")
usuario["ciudad"].append("bogota")

print(usuario)

usuario1 = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Colombia"
}

usuario2 = {
    "nombre": "Maria",
    "edad": 25,
    "ciudad": "México"
}

usuario3 = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Perú"
}

usuario4 = {
    "nombre": "Ana",
    "edad": 22,
    "ciudad": "Argentina"
}

usuario5 = {
    "nombre": "Luis",
    "edad": 35,
    "ciudad": "Chile"
}

personas.append(usuario1)
personas.append(usuario2)   
personas.append(usuario3)
personas.append(usuario4)
personas.append(usuario5)
