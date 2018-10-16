import numpy as np
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
        self.yIzq = []
        self.maxX = 0
        self.minX = 0

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

    def getMinX(self):
        #el x mas pequenio de la derecha C2
        temp = list(self.xDer)
        temp.sort()
        return(temp[0])

    def getMaxX(self):
        #el x mas grande de la izquierda c1
        temp = list(self.xIzq)
        temp.sort()
        return(temp[-1])


    def line(self):
        """
        https://www.reddit.com/r/learnpython/comments/298zbc/all_i_want_is_to_plot_a_simple_ymxb_function/

        http://code.activestate.com/lists/python-tutor/82380/
        """
        # min x y max x de los puntos de un lado para dividir $
        #x = np.linspace(int(self.getMinX()), int(self.getMaxX()))

        fig,ax = plt.subplots()
        ax.plot(self.x, self.m*self.x+self.b )
    
    def draw(self):
        self.getDer()
        self.getIzq()
        self.line()# linea divisoria
        plt.scatter(self.xIzq, self.yIzq, marker='o') #conjunto izquierdo
        plt.scatter(self.xDer, self.yDer, marker='^') #conjunto derecho
        plt.show()