#Crear una lista de 500 notas (1,5)
#Mock
import random 
notas=[]
for i in range (5):
    nota=random.randint(1,5)
    #LLenar una lista
    notas.append(nota)

#Manipulando listas con python
notas.insert(1,80)
notas.remove(80)
notas.pop(0)
notas.sort(reverse=True)
notas.clear()
print(notas)