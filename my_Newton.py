#!/usr/bin/python3.9
# Licence GPL-3 Copyright (c) 2022 Stéphane Lassalvy
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

# Fonction dont on cherche à résoudre f(x) = 0
def my_fonction(x):
  resultat = x**2 - 2*x -2
  return(resultat)

# Dérivée de la fonction précédente
def my_derivee(x):
  resultat = 2 * x - 2
  return(resultat)

# Algorithme de Newton pour résoudre l'équation de façon itérative
# x0 : point de départ
# f  : fonction dont on veut résoudre f(x) = 0
# fprime : fonction dérivée de f
# tol : tolérance, valeur pour laquelle on arrête l'algoritme si les écarts entre deux itérations consécutives |f(x(n+1)) - f(x(n))| <= tol ou |x(n+1) - x(n)| <= tol
# où x(n+1) et x(n) sont les approximation d'une valeur de x telle que f(x) = 0 aux itérations consécutives n+1 et au rang n
def my_Algo_Newton(x0, f, fprime, tol = 0.01):
    n = 0
    print(f"Le point de départ est x(0) = {x0}")
    print(f"Tolérance = {tol}")
    n = n + 1
    solution = x0 - f(x0) / fprime(x0)
    deltax = abs(solution - x0)
    deltaf = abs(f(solution) - f(x0))
    print(f"n = {n}")
    print(f"x({n}) = {solution}")
    print(f"x({n}) - x({n-1}) = {deltax}")
    print(f"f(x({n})) - f(x({n-1}) = {deltaf}")
    print(f"|f(x({n}) - 0| = {abs(f(solution))}")
    while(deltax > tol or deltaf > tol):
      n = n + 1
      solutionNew = solution - f(solution) / fprime(solution)
      deltax = abs(solutionNew - solution)
      deltaf = abs(f(solutionNew) - f(solution))
      solution = solutionNew
      print(f"n = {n}")
      print(f"x({n}) = ", solution)
      print(f"deltax = x({n}) - x({n-1}) = {deltax}")
      print(f"deltaf = f(x({n})) - f(x({n-1})) = {deltaf}")
      print(f"|f(x({n}) - 0| = {abs(f(solution))}")
    print(f"La solution approchée de x tel que f(x) = 0 est x({n})) = ", solution)
# Exécution du programme
my_Algo_Newton(2, my_fonction, my_derivee, tol = 0.001)
