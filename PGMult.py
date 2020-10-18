#Parámetros:
#Tamaño de la poblacion
DNA_SIZE        = 15  
#Generaciones
GENERACIONES     = 1000
#- Probabilidad de Cruzamiento: 0.4
torneo_SIZE = 5    
#- Probabilidad de Cruzamiento: 0.4
PROB_CRUZAMIENTO = 0.4 
#- Probabilidad de Mutacion: 0.4
PROB_MUTACION   = 0.4  
MIN       = 2    
MAX       = 5  
POP_SIZE = 10  
import random

#print ("Cantidad de Individuos : " + str(INDIVIDUOS))
print ("Cantidad de Genes por Individuo : " + str(DNA_SIZE))
print ("Probabilidad de Cruzamiento : " + str(PROB_CRUZAMIENTO))
print ("Probabilidad de mutación : " + str(PROB_MUTACION))
print ("Iteraciones  : " + str(GENERACIONES))
#print ("Matriz : " )
#print(matrix)
print("\n")
#ind = [["".join(random.sample('+−∗/+−∗/',DNA_SIZE)),0,0,0,0]for e in range(GENERACIONES)]
print("Poblacion Inicial: ")
#for e in ind:
#    print(e)
DNA_TAMANO        = 30  
# tiny genetic programming by © moshe sipper, www.moshesipper.com
from random import random, randint, seed
from statistics import mean
from copy import deepcopy



def sum(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y!=0 else 0
FUNCIONES = [sum, sub, mul, div]
SIMBOLOS = ["+", "-", "X","/"]
#TERMINALES = ['x',-5.0, -4.0, -3, 0, -2, -1, 1, 2, 3, 4, 5]
TERMINALES = ['x','y', 1, 2, 3, 4, 5]


def target_func(x,y): # evolution's target
    return x*x*x + x*y + y + 1

def muestras_funcion(): # generate 101 data points from target_func
    dataset = []
    for x in range(-100,101,2): 
        x /= 100
        dataset.append([x, x, target_func(x,x)])
    return dataset


'''
def muestras_funcion():
    dataset = [[	0	,	0	],
            [	0.1	,	0.005	],
            [	0.2	,	0.02	],
            [	0.3	,	0.045	],
            [	0.4	,	0.08	],
            [	0.5	,	0.125	],
            [	0.6	,	0.18	],
            [	0.7	,	0.245	],
            [	0.8	,	0.32	],
            [	0.9	,	0.405	],]
    
    return dataset
'''
def  generate_dataset():
    dataset = [[	0	,   1,	1	],
            [	0.1	,   2,	2.005	],
            [	0.2	,   3,	3.02	],
            [	0.3	,   4,	4.045	],
            [	0.4	,   5,	5.08	],
            [	0.5	,   6,	6.125	],
            [	0.6	,   7,	7.18	],
            [	0.7	,   8,	8.245	],
            [	0.8	,   9,	9.32	],
            [	0.9	,   10,	10.405	],]
    
    return dataset

class Arbol:
    def __init__(self, data = None, izq = None, der = None):
        self.data  = data
        self.izq  = izq
        self.der = der
        
    def nodo_etiqueta(self):
        if (self.data in FUNCIONES):
            if self.data.__name__ =="mul": 
                return "*"
            elif self.data.__name__ =="sum":
                return "+"
            elif self.data.__name__ =="sub":
                return "-"
            elif self.data.__name__ =="div":
                return "/"
        else: 
            return  str(self.data) 

    def imprimir(self,prefix=""): 
        #print("(",end="")
        print("(",end="")
        if self.izq:  self.izq.imprimir()
        print(self.nodo_etiqueta(),end="")        
        if self.der: self.der.imprimir()
        print(")",end="")

    def procesar_arbol(self, x, y): 
        if (self.data in FUNCIONES): 
            return self.data(self.izq.procesar_arbol(x, y), self.der.procesar_arbol(x, y))
        elif self.data == 'x': return x
        elif self.data == 'y': return y
        else: return self.data
            
    def arbol_aleatorio(self, grow, MAX, depth = 0):  #Generar una rama aleatoria
        if depth < MIN or (depth < MAX and not grow): 
            self.data = FUNCIONES[randint(0, len(FUNCIONES)-1)]
        elif depth >= MAX:   
            self.data = TERMINALES[randint(0, len(TERMINALES)-1)]
        else: 
            if random () > 0.5: 
                self.data = TERMINALES[randint(0, len(TERMINALES)-1)]
            else:
                self.data = FUNCIONES[randint(0, len(FUNCIONES)-1)]
        if self.data in FUNCIONES:
            self.izq = Arbol()          
            self.izq.arbol_aleatorio(grow, MAX, depth = depth + 1)            
            self.der = Arbol()
            self.der.arbol_aleatorio(grow, MAX, depth = depth + 1)

    def mutacion(self):
        #print("mutacion")
        if random() < PROB_MUTACION: 
            self.arbol_aleatorio(grow = True, MAX = 2)
        
        elif self.izq: self.izq.mutacion()
        elif self.der: self.der.mutacion() 

    def size(self): 
        if self.data in TERMINALES: return 1
        l = self.izq.size()  if self.izq  else 0
        r = self.der.size() if self.der else 0
        return 1 + l + r

    def crear_subarbol(self): 
        t = Arbol()
        t.data = self.data
        if self.izq:  t.izq  = self.izq.crear_subarbol()
        if self.der: t.der = self.der.crear_subarbol()
        return t
                        
    def escanear_arbol(self, count, second): 
        count[0] -= 1            
        if count[0] <= 1: 
            if not second: 
                return self.crear_subarbol()
            else:
                self.data  = second.data
                self.izq  = second.izq
                self.der = second.der
        else:  
            ret = None              
            if self.izq  and count[0] > 1: ret = self.izq.escanear_arbol(count, second)  
            if self.der and count[0] > 1: ret = self.der.escanear_arbol(count, second)  
            return ret

    def cruzamiento(self, other): 
        if random() < PROB_CRUZAMIENTO:
            #print("Cruzamiento")
            aux = self.izq 
            second = other.escanear_arbol([randint(1, other.size())], None)
            self.izq = other.izq
            other.izq = aux

def inicializar_poblacion(): 
    pop = []
    for md in range(3, MAX + 1):
        for i in range(int(DNA_TAMANO/6)):
            t = Arbol()
            t.arbol_aleatorio(grow = True, MAX = 2) 
            pop.append(t) 
        for i in range(int(DNA_TAMANO/6)):
            t = Arbol()
            t.arbol_aleatorio(grow = False, MAX = 2) 
            pop.append(t) 
    return pop

def fitness(individual, dataset): 
    return 1 / (1 + mean([abs(individual.procesar_arbol(ds[0], ds[1]) - ds[2]) for ds in dataset]))
                
def seleccion(poblacion, fitnesses): 
    torneo = [randint(0, len(poblacion)-1) for i in range(torneo_SIZE)] 
    torneo_fitnesses = [fitnesses[torneo[i]] for i in range(torneo_SIZE)]
    return deepcopy(poblacion[torneo[torneo_fitnesses.index(max(torneo_fitnesses))]]) 
            
def main():      
    seed() 
    dataset = muestras_funcion()
    poblacion= inicializar_poblacion() 
    mejor = None
    mejor_f = 0
    mejor_gen = 0
    fitnesses = [fitness(poblacion[i], dataset) for i in range(DNA_TAMANO)]
    print("Poblacion inicial")
    #print(poblacion[1].imprimirp())
    print("Calcular la Aptitud para cada Individudo")
    print(fitnesses)
    # go evolution!
    for gen in range(GENERACIONES):        
        nextgen_poblacion=[]
        for i in range(DNA_TAMANO):
            parent1 = seleccion(poblacion, fitnesses)
            parent2 = seleccion(poblacion, fitnesses)
            parent1.cruzamiento(parent2)
            parent1.mutacion()
            nextgen_poblacion.append(parent1)
        poblacion=nextgen_poblacion
        fitnesses = [fitness(poblacion[i], dataset) for i in range(DNA_TAMANO)]
        print("\nNueva poblacion")
        #print("\n**** Iteración ",gen,"****")
        for popu in range(POP_SIZE):
            poblacion[popu].imprimir()
            print("")
        if max(fitnesses) > mejor_f:
            mejor_f = max(fitnesses)
            mejor_gen = gen
            mejor = deepcopy(poblacion[fitnesses.index(max(fitnesses))])
        print("\nCalcular la Aptitud para cada Individuo")
        for fit in range(POP_SIZE):
            print(1-fitnesses[fit])
        
    
    print("\nMejor solucion")
    mejor.imprimir()
    
if __name__== "__main__":
  main()