# Fastplots

## ¿Qué es fastplots?

Es una librería de Python que utiliza ```matplotlib.pyplot``` para hacer gráficos rápidamente con gran versatilidad, pudiendo hacer gráficos simples o complejos en poco tiempo comparado con el uso estándar de ```matplotlib```.

## ¿Por qué usar fastplots?

Supongamos que tiene unos datos dados por los arreglos ```a=np.arange(100)``` y ```b=a**2```, es decir, una curva cuadrática con x=[0,100]. Si quisiera graficar estos datos con su respectivo título, leyenda, márgenes, labels y su trazo de línea favorito, su código debería ser algo así:

```python
import matplotlib.pyplot as plt

plt.plot(a,b,".",label="Cuadrática")
plt.xlim(-10,110)
plt.ylim(-500,10300)
plt.title("Ensayo")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.grid()
plt.show()
```

Con ```fastplots``` todo lo que debe escribir para lograr un resultado **exactamente igual al anterior** es:

```python
from fastplots import grafico

grafico(a,b,".",leyenda="Cuadrática",xmargen=10,ymargen=5,
        titulo="Ensayo",xlabel="Eje x",ylabel="Eje y")
```


## Funciones
## ```grafico```
Muestra un gráfico de ```plt.plot``` de dos arreglos que se quiera, siempre que tengan la misma longitud.

### Argumentos:

Los marcados con * son obligatorios. El resto, opcionales.

Argumento | Tipo de dato | Descripción
:----: | :----: | :----: |
```a```, ```b```* | Arreglo | Los arreglos a graficar para los ejes _x_ e _y_ respectivamente. En esencia, ```grafico(a,b)``` es igual a ```plt.plot(a,b,".")```
```linea``` | Caracter | Dicta el tipo de trazo (por ejemplo, "o", ".", "-", "--", ...).
```leyenda``` | Cadena | Establece el nombre que quiera ponerle a la línea.
```xmargen```, ```ymargen``` | Entero o float | En porcentaje, establece el rango a graficar. Si ```xmargen=5```, la curva tendrá un 5% de espacio a ambos lados sobre el eje x respecto al rango total de los elementos graficados. De no ser especificados, se dejará el margen que asignen ```plt.xlim``` y ```plt.ylim``` por defecto.
```titulo``` | Cadena | Establece el título del gráfico.
```xlabel```, ```ylabel``` | Cadena | Establece los títulos de los ejes _x_ e _y_ respectivamente.
```grid``` | Booleano | Pone cuadrícula en el gráfico. El valor por defecto es ```True```. Se puede desactivar con ```grid=False```.
