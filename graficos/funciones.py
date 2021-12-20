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
  
  
def grafico_multilineas(t,ys,trazos="",titulo=None,leyendas=None,xlabel=None,ylabel=None,grid=True,margen=0):
  """Genera un gráfico con varias curvas, usando un array para el eje x y los
  demás para el eje y.
  
  Parámetros
  ----------
  Obligatorios:
  t : lista o np.array
    El array usado para el eje x.
  ys : listas a graficar respecto a t.
    Los arrays usados para el eje y. Si a y b son listas, se pasan como (a,b).
  
  Opcionales:
  trazos : lista de str
    Los trazos que se deseen para todas las líneas, p.e. ".", "o", "-r", etc.
  titulo : str
    título del gráfico
  leyendas : lista de str
    Los nombres de las curvas que aparecerán en el gráfico.
  xlabel : str
    título del eje x
  ylabel : str
    título del eje y
  grid : boolean
    Por defecto en True. Se puede desactivar pasando el argumento grid=True
  margen : int o float
    Determina los márgenes alrededor de la curva. Por defecto en 0.
  """

  fig, ax = plt.subplots()
  # ¿Con o sin leyenda?
  if leyendas==None:
    for i,y in enumerate(ys):
      ax.plot(t,y,trazos[i])
  else:
    for i,y in enumerate(ys):
      ax.plot(t,y,trazos[i],label=leyendas[i])
    ax.legend()
  # Textos del gráfico
  fig.suptitle(titulo)
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  # ¿Con o sin cuadrícula?
  if grid==True:
    ax.grid()
  ax.margins(margen)
  plt.show()
