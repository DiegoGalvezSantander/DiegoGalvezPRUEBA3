import json



def agregarCategoria(nombre:int):
    with open("biblioteca.json",mode="r") as lecturaJson:
        archivoJson = json.load(lecturaJson)

        categoria_nueva = {
                "id": len(archivoJson["Categoria"])+1,
                "nombre": nombre,
                
            }
        
        archivoJson["Categoria"].append(categoria_nueva)

    with open("biblioteca.json",mode="w") as escribirJson:
        json.dump(archivoJson,escribirJson, indent=4)

def editarCategoria(id:int,nombre:str):
    with open("biblioteca.json",mode="r") as lecturaJson:
        archivoJson = json.load(lecturaJson)
        contador=0
        for i in archivoJson["Categorias"]:
            if i["id"]==id:
                print("encontrado")
        contador+=1
    archivoJson["Categorias"][contador]["nombre"]=nombre
    with open("biblioteca.json",mode="w") as escribirJson:
        json.dump(archivoJson,escribirJson, indent=4)
def eliminarCategoria(id:int):
    with open("biblioteca.json",mode="r") as lecturaJson:
        archivoJson = json.load(lecturaJson)

    contador=0
    
    for i in archivoJson["Categorias"]:
       if i["id"]==id:
           print("encontrado")
           
    contador+=1
    print(contador)
    archivoJson["Categorias"].pop(contador)
    with open("biblioteca.json",mode="w") as escribirJson:
        json.dump(archivoJson,escribirJson, indent=4)     
def listadoCategorias():
    with open("biblioteca.json",mode="r") as lecturaJson:
        archivoJson = json.load(lecturaJson)

    for i in archivoJson["Categorias"]:

        print(i(["id"]),i(["nombre"]))
    listadoCategorias()
    
    with open("biblioteca.json",mode="w") as escribirJson:
        json.dump(archivoJson,escribirJson, indent=4)

    





     





    
