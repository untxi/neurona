import random
class GenTuples:
    def __init__(self):
        self.fileName = ""  
    
    def createFile(self, nameToSave):
        self.file = open((nameToSave + ".tdata"), "w")
    
    def writeFile(self, words):
        self.file.write(words)
    
    def finish(self):
        self.file.close()

    def addTuple(self, x, y):
        self.file.write('('+str(x)+','+str(y)+') ')

    def addMultiTuple(self):
        print("Write tuple: 'x,y', if job is done write 'end'")
        run = True
        while run:
            opt = str(input(">> "))
            print(opt)
            if opt != "end":
                self.file.write(opt + ' ')
            else:
                run = False
    
    def auto(self):
        self.createFile("autoC1")
        for num in range(50):
            xRand = random.randint(-100,100)
            yRand = random.randint(-100,100)
            self.addTuple(xRand, yRand)
        self.finish()

        self.createFile("autoC2")
        for num in range(50):
            xRand = random.randint(-100,100)
            yRand = random.randint(-100,100)
            self.addTuple(xRand, yRand)
        self.finish()