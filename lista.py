listafruta = ["banana", "piña", "naranja", "uva",  "mango", "pera", "manzana",]

listafruta.append("melon")
for fruta in listafruta:
    print(f"fruta: {fruta}")    

listafruta[5] = "fresa"
for fruta in listafruta:
    print(f"fruta: {fruta}")    
