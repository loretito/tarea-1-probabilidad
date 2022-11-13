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

#se crean dos diccionarios con las llaves de 10 a 60 y con valor 0
# uno de ellos para realizar el calculo de la frecuencia y el otro para el calculo de la esperanza
data = {}    
newData = {}
for i in range(10,61):
    data[i] = 0
    newData[i] = 0

#esta funcion va sumando cuantas veces se repite x resultado 
#(frecuencia absoluta) y lo guarda como valor en el diccionario anterior

def frec_abs(datos):  
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

esperanza = [] #un arreglo vacio, donde se almacenaran las probabilidades de cada valor

for a in range(1, 7):  #se hacen 10 for que le dan valores a los dados para calcular las combinaciones posibles de suma
    d1 = a 
    for b in range(1, 7):
        d2 = b 
        for c in range(1, 7):
            d3 = c 
            for d in range(1, 7):
                d4 = d 
                for e in range(1, 7):
                    d5= e 
                    for f in range(1, 7):
                        d6 = f 
                        for g in range(1, 7):
                            d7 = g
                            for h in range(1, 7):
                                d8 = h 
                                for i in range(1, 7):
                                    d9 = i 
                                    for j in range(1, 7):
                                        d10 = j;
                                        suma = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 
                                        newData[suma] += 1   #se va agregando la combinacion al posible resultado 
                                        
y1 = list(newData.values()) #se guardan las combinaciones posibles

for i in range(0, len(x)):  
    esperanza.append((y1[i]/60466176)*x[i]) #se calcula la esperanza de cada valor, y se divide por el total de combinaciones posibles y se multiplica por el x 

plt.plot(x,esperanza)
plt.xlabel('x')
plt.ylabel('Esperanza') 
plt.title('Esperanza de cada valor')
plt.show()
