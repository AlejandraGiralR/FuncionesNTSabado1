#crear unalista de 500 notas (1,5)
#Mock
import random

notas=[]
for i in range(5):
    #nota=round(random.uniform(1.0,5.0),1) # flotante redondeado a 1 decimal
    nota = random.randint(1,5)
    #llenar una lista
    notas.append(nota)
#print(notas)

#Manipulando listas con python
notas.insert(1,80)
notas.remove(80)
notas.pop(0)
notas.sort(reverse=True)
notas.clear()
print(notas)