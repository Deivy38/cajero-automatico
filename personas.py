personas = []

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