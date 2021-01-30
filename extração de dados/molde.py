#s = "0,010070801;1,545479996;-0,000265045;1;1;0,005809117;-0,005269692;1 mA\n"


import pandas as pd
import matplotlib.pyplot as plt

def plotar(self):
        
        #locx = self.txt + ".txt"
                
                plt.plot.__init__()
                pd.read_csv.__init__()
                
                dados = pd.read_csv(self.txt, header=0, encoding = 'unicode_escape', delimiter=";")
                l = [x for x in dados.columns]
        
                plt.plot(dados[l[0]], dados[l[2]])
                plt.title("A x V")
                plt.grid()

                plt.savefig(self.texto + ".png")

                del self.txt
                del self.texto
                del dados
                del l

def ajeitar(s):
        modificar = s.split(";")
        cont = len(modificar)
        s = ""
        l = [n.replace(",", ".") for n in modificar]
        l[-1] = l[-1][:-1]
        ln = [i.strip() for i in l]
        l = ln
        del ln
        #print(l)
        for i in range(cont):
            if True:
                s += l[i] + ";"
        s = s[:-1]
        #print(s)
        return s

class Modelo(object):
    
        def __init__(self, csv, txt):
                self.csv = csv
                self.txt = txt + '.txt'
                self.texto = txt
                self.c = 0
        
        def extracao(self):
                with open(self.csv, 'r') as a, open(self.txt, 'w+') as b:
                        for linhas in a:

                                if self.c > 0:
                                        nova = ajeitar(linhas)
                                        print(nova)
                                        b.write(nova + "\n")
                                else:
                                        b.write(linhas)
                                        self.c += 1

            
        def plotar(self):
        
        #locx = self.txt + ".txt"
                #plt.pause(0.05)
                #plt.plot.__init__()
                #pd.read_csv.__init__()
                #fig = plt.figure(figsize=(20, 10))

                #ax1 = fig.add_subplot(1,2,1)

                #ax1 = fig.add_subplot()
            
                fig, ax1 = plt.subplots(figsize=(8.0,5.0))
                #fig, ax1 = plt.subplots(figsize=(8.0,5.0), dpi=200.0)
                
                dados = pd.read_csv(self.txt, header=0, encoding = 'unicode_escape', delimiter=";")
                l = [x for x in dados.columns]
                
                ax1.plot(dados[l[0]], dados[l[2]])
                ax1.set_title("Voltametria Ciclica")
                ax1.set_xlabel(l[0])
                ax1.set_ylabel(l[2])
                
                #plt.pause(0.05)
                ax1.grid()

                plt.savefig(self.texto + ".png")

                del self.txt
                del self.texto
                del dados
                del l
                del ax1
#--------------
