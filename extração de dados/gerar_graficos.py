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
