#funciones ue crea lista de N notas
import random

def crear_lista_notas(numeroNotas):
    notas=[0]
    for _ in range(numeroNotas):
        notas=random.randint(1,5)
        notas.append(nota)
    return notas

