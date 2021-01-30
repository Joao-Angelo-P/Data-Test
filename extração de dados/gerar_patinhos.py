'''
def func(word, freq=1, add=0):
    __vetor = word*(freq + add)
    t__vetor = len(__vetor)/len(word)
    # print(word*(freq + add))
    cont = 0
    s = ''
    print(f'Vetor String: {__vetor}')
    print(f'\'{word}\' se repete {t__vetor:.0f} vezes.')
    for i in __vetor:
        s += i
        if s == 'hello':
            cont += 1
            s = ''
    print(f'Vezes: {cont}')

func('hello', 5, 3)
# print(call)
'''
'''
try:
    def a(n): return b(n)
    def b(n): return c(n)
    def c(n): return 1/n
    a(int(input()))
except:
    print('Divisão incorreta n = 0: 1/0')

'''


'''
r = True
while r:
    import numpy as np

    print('\t7x + 3y = 23\n\t15x - 2y = 24\n\n')
    #################
    A = np.array([7,3,15,-2])
    A = A.reshape(2,2)
    c = np.array([23,24])
    c = c.reshape(2,1)
    soluçao = np.linalg.solve(A,c)
    soluçao = soluçao.reshape(1,2)
    letras = str(soluçao)
    letras = letras.strip('[]')
    letra = letras[0] + ',' + letras[3]

    #################
    print(F'\tChemistry\u207D\u1d49\u207f\u1d4d\u2071\u207f\u1d49\u1d49\u02b3\u2071\u207f\u1d4d\u207E')
    print(F' \nMatriz das incognitas:\n{A}\n\n Matriz dos coeficientes:\n{c}\n\n Solução do sistema: ({letra})')
    r = int(input(""))
'''

import glob
import molde as m
r = ""

l = glob.glob("*.csv")

def reiniciar():
    import os
    l_fotos = glob.glob("*.png")
    l_T = glob.glob("*.txt")
    for i in range(len(l_T)):
        os.remove(l_T[i])
        os.remove(l_fotos[i])


'''
a = m.Modelo(l[i], l[i][:-4])
    a.extracao()
    a.plotar()
'''
def fazer():
    for i in range(len(l)):
        m.Modelo(l[i], l[i][:-4]).extracao()
        m.Modelo(l[i], l[i][:-4]).plotar()


while  True:
    print("Deseja Executar:\n[1]Gerar Arquivos .txt e .png\n[2]Apagar Arquivos .txt e .png\n[3]Sair\n")
    resposta = input()
    
    
    if resposta == "1":
        fazer()
    
    elif resposta == "2":
        reiniciar()
        
    elif resposta == "3":
        break
