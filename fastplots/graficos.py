import numpy as np
import matplotlib.pyplot as plt

def margen(arreglo,porcentaje=5):
    """Dado un arreglo, establece valores que se pueden usar para plt.xlim y
    plt.ylim que son márgenes de un porcentaje del rango total del arreglo.

    Parámetros
    ----------
    arreglo : lista o numpy.ndarray
      El arreglo que se pretende graficar
    porcentaje: int o float, opcional
      Si no se especifica, su valor por defecto es 5.

    Retorna
    ----------
    -minimo-porciento : float
    maximo+porciento : float

    Ejemplo:
    Sea a=np.arange(-20,81) y porcentaje=5
    Entonces minimo=-20 y maximo=80
    El rango completo del arreglo es 80-(-20)=100. Por tanto, el 5% del rango
    del arreglo completo es 5. Entonces esta función retorna (-25,85).
    """

    minimo = min(arreglo)
    maximo = max(arreglo)
    porciento = porcentaje*(maximo-minimo)/100
    return (-minimo-porciento, maximo+porciento)


def grafico(a,b,trazo=".",leyenda=None,xmargen=None,ymargen=None,
            titulo=None,xlabel=None,ylabel=None,grid=True):
    """Genera un gráfico tipo plt.plot.

    Parámetros
    ----------
    Obligatorios:
    a, b : numpy.ndarray
      Los arreglos a graficar

    Opcionales:
    trazo : str
      El trazo que se desea, p.e. ".", "o", "-r", etc.
    leyenda : str
    xmargen, ymargen : int o float
      los márgenes que se deseen para el gráfico, determinados por
      la función margen()
    titulo : str
      título del gráfico
    xlabel : str
      título del eje x
    ylabel : str
      título del eje y
    grid : boolean
      Por defecto en True. Se puede desactivar pasando el argumento grid=True
    """
    
    # ¿con o sin leyenda?
    if leyenda!=None:
        plt.plot(a,b,trazo,label=leyenda)
        plt.legend()
    else: plt.plot(a,b,trazo)
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
    # cantidad de intervalos
    if num_intervalos==None:
        plt.hist(datos,density=normalizada)
    else:
        plt.hist(datos,bins=num_intervalos,density=normalizada)
    # títulos y labels
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # ¿con o sin grid?
    if grid==True: plt.grid()
