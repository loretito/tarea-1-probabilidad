import matplotlib.pyplot as plt
import random as r

def sumaDados(): 
    suma = 0
    for i in range(0,10): #aqui se suman los 10 dados
        suma+= r.randint(1,6) #salen numeros random del 1 al 6
    return suma

datos = []

for i in range(0, 10000): 
    datos.append(sumaDados())  #se guardan los 10000 resultados


data = {}                   #se crea un diccionario con las llaves de 10 a 60 y con valor 0 
for i in range(10,61):
    data[i] = 0

def frec_abs(datos):  #esta funcion va sumando cuantas veces se repite x resultado (frecuencia absoluta) y lo guarda como valor en el diccionario anterior
    for i in datos:
        if (i in data):   
            data[i] += 1 
        else: 
            data[i] = 1 
    return data  

d = frec_abs(datos) #se guarda el nuevo diccionario 

x = list(d.keys())  #x guarda las llaves (los posibles resultados)
y =  list(d.values()) #y guarda los valores (las frecuencias absolutas)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('frec. absoluta')
plt.title('Suma dados')
plt.show()

#ahora calculamos la esperanza de cada valor 

esperanza = [] #un arreglo vacio 

for i in range(0, len(x)):  
    esperanza.append((y[i]/10000)*x[i])    #se recorre el array de x e y, y se divide por 10000 para obtener la probabilidad y se multiplica por x

plt.plot(x,esperanza)
plt.xlabel('x')
plt.ylabel('Esperanza') 
plt.title('Esperanza de cada valor')
plt.show()