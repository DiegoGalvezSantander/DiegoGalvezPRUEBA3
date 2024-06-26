import mantenedores
while True:
    print("MUNDO LIBRO")
    print("1. Mantenedor de categorias")
    print("2. Reportes")
    print("3. Salir")
    opcion=int(input("ingrese una opcion : "))

    if opcion==1:
     while True:
        print("1. Agregar categoria")
        print("2. Editar categoria")
        print("3. Eliminar categoria ")
        print("4. Listar ")
        print( "5.Volver")
        opcionCategorias=int(input("ingrese una opcion : "))
        if opcionCategorias==1:
          nombre=input("ingrese el nombre de la nueva categoria: ")
          mantenedores.agregarCategoria(nombre)
        if opcionCategorias==2:
         id=int(input("ingrese el id"))
         nombre=input("nuevo nombre de la categoria")
         mantenedores.editarCategoria


        if opcionCategorias==3:
         id=int(input("ingrese el id que quiere borrar: "))
         mantenedores.eliminarCategoria(id)
        if opcionCategorias==4:
         mantenedores.listadoCategorias()
        if opcionCategorias==5:
         break
    if opcion==2:
      print("No implementado")
    if opcion==3:
      break


