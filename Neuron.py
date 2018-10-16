import random

class Neuron():
    def __init__(self):
        self.realDataC1 = []
        self.realDataC2 = []
        self.realData   = []
        self.x  = 0
        self.y  = 0
        self.b  = 1
        self.w1 = 0
        self.w2 = 0
        self.d  = 0
        self.m  = 0

    
    def realDataUpdate(self):
        self.realData = self.realDataC1 + self.realDataC2
    
    def addConjC1(self, newPoint):
        self.realDataC1.append(newPoint)
        self.realDataUpdate()
    
    def addConjC2(self, newPoint):
        self.realDataC2.append(newPoint)
        self.realDataUpdate()

    def setConjD(self, listD):
        self.realData = listD
    
    def setConjC1(self, listC1):
        self.realDataC1 = listC1
    
    def setConjC2(self, listC2):
        self.realDataC2 = listC2

    def setConjuts(self, listD, listC1, listC2):
        self.realData = listD
        self.realDataC1 = listC1
        self.realDataC2 = listC2

    def showData(self):
        print (self.realData)

    def showC1(self):
        print (self.realDataC1)

    def showC2(self):
        print (self.realDataC2)

    def getConjD(self):
        return self.realData

    def getConjC1(self):
        return self.realDataC1
 
    def getConjC2(self):
        return self.realDataC2

    def classify(self):
        temp = (self.x * self.w1) + (self.y * self.w2) + self.b
        if temp >= 0:
            return 1
        if temp < 0:
            return -1
    
    def correction(self, point):        
        if (point in self.realDataC2) and self.y == -1:
                self.d = 1
        if (point in self.realDataC2) and self.y == 1:
                self.d = -1

        self.w1 = self.w1 + self.d * self.x
        self.w2 = self.w2 + self.d * self.y
        self.b  = self.b  + self.d
        
    def getM(self):
        self.m = (- self.w1) / self.w2
        return self.m

    def training(self):
        self.w1 = random.random()
        self.w2 = random.random()
        self.b  = random.random()

        for point in self.realData:
            self.x = point[0]
            self.y = point[1]
            self.correction(point)

            self.getM()
            """
            print("x:" + str(self.x))
            print("m:" + str(self.m))
            print("b:" + str(self.b))
            print("y:" + str(self.y))
            """

       
    
    