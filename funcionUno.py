def crear_lista_estudiantes(numeroEstudiantes):
    estudiantes=[]
    for _ in range(numeroEstudiantes):
        estudiante={}
        estudiante["id"]=input("Digita tu id: ")
        estudiante["nombres"]=input("Digita tu nombre: ")
        estudiante["documento"]=input("Digita tu documento: ")
        estudiante["semestre"]=input("Digita tu semestre: ")
        estudiantes.append(estudiante)
    
    return estudiantes

crear_lista_estudiantes(5)