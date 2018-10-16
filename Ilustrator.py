import matplotlib.pyplot as plt
import Neuron

class Ilustrator:
    

    def __init__(self):
        self.puntosIzq = []
        self.puntosDer = []
        #linea
        self.y = 0
        self.x = 0
        self.m = 0
        self.b = 0
        # para puntos
        self.xDer = []
        self.yDer = []
        self.xIzq = []
        self.yIzq= []

    def setValues(self, newNeuron):
        self.puntosIzq = newNeuron.getConjC1()
        self.puntosDer = newNeuron.getConjC2()
        #linea
        self.y = newNeuron.y
        self.x = newNeuron.x
        self.m = int(newNeuron.m)
        self.b = int(newNeuron.b)

    def showLinea(self):
        print("x:" + str(self.x))
        print("m:" + str(self.m))
        print("b:" + str(self.b))
        print("y:" + str(self.y))

    def getIzq(self):
        for point in self.puntosIzq:
            self.xIzq.append(point[0])
            self.yIzq.append(point[1])

    def getDer(self):
        for point in self.puntosDer:
            self.xDer.append(point[0])
            self.yDer.append(point[1])

    
    def draw(self):
        self.getDer()
        self.getIzq()
        plt.plot(self.x, self.y) # linea divisoria
        plt.scatter(self.xIzq, self.yIzq, marker='o') #conjunto izquierdo
        plt.scatter(self.xDer, self.yDer, marker='^') #conjunto derecho
        plt.show()


#working on line
def auxLine():
    import numpy as np
    import matplotlib.pyplot as plt

    AB = np.random.randn(100,2) #create a random array of [[A1,B1],[A2,B2],...] as $

    x = np.linspace(-100.,100.)

    fig,ax = plt.subplots()
    ax.plot(x, 13*x+10 )

    ax.set_xlim((-100.,100.))
    ax.set_ylim((-100.,100.))

    plt.show()