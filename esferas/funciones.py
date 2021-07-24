"""Contiene fórmulas para calcular perímetros, áreas y volúmenes
de círculos, sectores circulas, esferas y casquetes esféricos.
"""

from math import pi

def circulo_perimetro(r):
  """Calcula el perímetro de un círculo de radio r.

  Parámetros
  ----------
  r : int o float
    Radio del círculo.

  Retorna
  -------
  perimetro : float
    Perímetro del círculo.
  """

  perimetro = pi*r**2
  return perimetro


def circulo_area(r):
  """Calcula el área de un círculo de radio r.

  Parámetros
  ----------
  r : int o float
    Radio del círculo.

  Retorna
  -------
  area : float
    Área del círculo.
  """

  area = 2*pi*r
  return area


def sector_area(r,theta):
  """Calcula el área de un sector circular (theta en radianes).

  Parámetros
  ----------
  r : int o float
    Radio del círculo.
  theta : int o float
    Ángulo del sector circular.

  Retorna
  -------
  area : float
    Área del sector esférico.
  """

  area = r**2*theta/2
  return area


def esfera_superficie(r):
  """Calcula el área superficial de una esfera de radio r.

  Parámetros
  ----------
  r : int o float
    Radio de la esfera.

  Retorna
  -------
  area : float
    Área superficial de la esfera.
  """
  
  area = 4*pi*r**2
  return area


def esfera_volumen(r):
  """Calcula el volumen de una esfera de radio r.

  Parámetros
  ----------
  r : int o float
    Radio de la esfera.

  Retorna
  -------
  volumen : float
    Volumen de la esfera.
  """

  volumen = 4*pi*r**3/3
  return volumen


def casquete_area(r,h):
  """Calcula el área superficial de un casquete esférico con el radio de la 
  esfera de la que se tomó y la altura del casquete.

  Parámetros
  ----------
  r : int o float
    Radio de la esfera.
  h : int o float
    Altura del casquete.

  Retorna
  -------
  area : float
    Área del casquete esférico
  """

  area = 2*pi*r*h
  return area


def esfera_radio_casquete(a,h):
  """Calcula el radio de una esfera con el radio y la altura de un casquete
  tomado de dicha esfera.

  Parámetros
  ----------
  a : int o float
    Radio del casquete.
  h : int o float
    Altura del casquete.

  Retorna
  -------
  area : float
    Radio de la esfera.
  """

  radio = (a**2+h**2)/(2*h)
  return radio


def casquete_area2(a,h):
  """Calcula el área superficial de un casquete esférico con su radio y altura.

  Parámetros
  ----------
  a : int o float
    Radio del casquete.
  h : int o float
    Altura del casquete.

  Retorna
  -------
  area : float
    Área del casquete.
  """

  area = (a**2+h**2)*pi
  return area


def casquete_volumen(a,h):
  """Calcula el volumen de un casquete esférico con su radio y altura.

  Parámetros
  ----------
  a : int o float
    Radio del casquete.
  h : int o float
    Altura del casquete.

  Retorna
  -------
  volumen : float
    Volumen del casquete.
  """

  volumen = pi*h*(3*a**2+h**2)/6
  return volumen


def casquete_volumen2(r,h):
  """Calcula el volumen de un casquete esférico con el radio de la esfera de la
  que se tomó y la altura del casquete.

  Parámetros
  ----------
  r : int o float
    Radio de la esfera.
  h : int o float
    Altura del casquete.

  Retorna
  -------
  volumen : float
    Volumen del casquete.
  """

  volumen = pi*h**2*(3*r-h)/3
  return volumen
