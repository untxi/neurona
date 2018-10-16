from GenTuples import *
from ExtractData import *
from Ilustrator import *
from Neuron import *

myIlustrator = Ilustrator()
myAuto = GenTuples()
myData = ExtractData()
myMind = Neuron()
myAuto.auto()

#Esto es para entrenar la neurona
myData.setFile("originalC1.tdata")
myData.readData(1)
myMind.setConjC1(myData.getConjC1())
myData.setFile("originalC2.tdata")
myData.readData(2)
myMind.setConjC2(myData.getConjC2())
myMind.setConjD(myData.getConjD())

myMind.training()
#ilustrar entrenamiento
myIlustrator.setValues(myMind)
myIlustrator.showLinea()
myIlustrator.draw()


# Puntos nuevos
myData.setFile("autoC1.tdata")
myData.readData(1)
myMind.setConjC1(myData.getConjC1())
myData.setFile("autoC2.tdata")
myData.readData(2)
myMind.setConjC2(myData.getConjC2())

#cambiar trainig por algo que clasifique
myMind.training() 

# muestra el nuevo resultado
myIlustrator.setValues(myMind)
myIlustrator.showLinea()
myIlustrator.draw()