import numpy as np
import matplotlib.pyplot as plt

def grafico(x,y,trazo="",titulo=None,leyenda=None,xlabel=None,ylabel=None,grid=True,margen=0):
  """Genera un gráfico simple.
  
  Parámetros
  ----------
  Obligatorios:
  x, y : listas o arreglos de numpy
    Los arreglos a graficar

  Opcionales:
  trazos : str
    El trazo que se desea. Por ejemplo, "*", "-r", "--b", etc.
  titulo : str
    Título del gráfico
  leyenda : str
    El nombre de la curva que aparecerá como leyenda en el gráfico
  xlabel, ylabel : str
    Títulos de los ejes respectivos
  grid : boolean
    Determina si se muestra la cuadrícula. Por defecto en True.
  margen : int o float
    Determina los márgenes alrededor de la curva. Por defecto en 0.
   """

  fig, ax = plt.subplots()
  ax.plot(x,y,trazo,label=leyenda)
  # Textos del gráfico
  fig.suptitle(titulo)
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  # ¿Con o sin leyenda?
  if leyenda!=None:
    ax.legend()
  # ¿Con o sin cuadrícula?
  if grid==True: ax.grid()
  ax.margins(margen)
  plt.show()
