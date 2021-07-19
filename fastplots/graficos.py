import numpy as np
import matplotlib.pyplot as plt

def margen(arreglo,porcentaje):
    minimo = min(arreglo)
    maximo = max(arreglo)
    porciento = porcentaje*(maximo-minimo)/100
    return (-minimo-porciento, maximo+porciento)

def grafico(a,b,linea=".",leyenda=None,xmargen=None,ymargen=None,titulo=None,xlabel=None,ylabel=None,grid=True):
    
    # ¿con o sin leyenda?
    if leyenda!=None:
        plt.plot(a,b,linea,label=leyenda)
        plt.legend()
    else: plt.plot(a,b,linea)
        
    # títulos y labels
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # márgenes
    if xmargen!=None:
        plt.xlim(margen(a,xmargen))
    if ymargen!=None:
        plt.ylim(margen(b,ymargen))
        
    # ¿con o sin grid?
    if grid==True: plt.grid()
    
    plt.show()
