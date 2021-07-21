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

    def grafico_multilineas(t,ys,trazo=".",leyendas=None,titulo=None,xlabel=None,ylabel=None,grid=True):
    
    # ¿con leyenda?
    if leyendas==None:
        for i,array in enumerate(ys):
            plt.plot(t,array,trazo)
    else:
        for i,array in enumerate(ys):
            plt.plot(t,array,trazo,label=leyendas[i])
        plt.legend()
        
    # títulos y labels
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # ¿con grid?
    if grid==True: plt.grid()
    
    plt.show()
    
    
def histograma(datos,num_intervalos=None,normalizada=False,titulo=None,xlabel=None,ylabel=None,grid=True):
    if num_intervalos==None:
        plt.hist(datos,density=normalizada)
    else:
        plt.hist(datos,bins=num_intervalos,density=normalizada)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if grid==True: plt.grid()
