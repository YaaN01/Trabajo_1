#main
import networkx as nx
import matplotlib.pyplot as plt
import time
from graph import ES
from utils import camino_mas_rapido, backtracking_tsp, resolver_tsp_backtracking, nearest_neighbor_tsp

#Aquí se compararán los tres métodos definidos para encontrar la ruta más rápida en una red de carreteras

#Primero, la distancia de una ciudad a otra, el caso más simple:

problema1 = ["Madrid", "Valencia"]

t1=time.perf_counter()
x, y = camino_mas_rapido(ES, "Madrid", "Valencia")
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in y:
    rec= rec + elements + " "

print("Problema 1: Distancia de Madrid a Valencia.\n")
print("Método de Dijkstra:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {x}min.")
print(f"   Tiempo tardado: {t}ms")

t1 = time.perf_counter()
x, y = resolver_tsp_backtracking(ES, camino_mas_rapido, "Madrid", problema1)
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in x:
    rec= rec + elements + " "

print("\nMétodo TSP Backtracking:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {y}min.")
print(f"   Tiempo tardado: {t}ms")

t1 = time.perf_counter()
x, y = nearest_neighbor_tsp(ES, camino_mas_rapido, "Madrid", problema1)
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in x:
    rec= rec + elements + " "

print("\nMétodo TSP Nearest Neighbor:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {y}min.")
print(f"   Tiempo tardado: {t}ms")

#El tiempo que calcula TSP es el doble porque está haciendo un recorrido cerrado (vuelve al inicio), y tampoco sale la ciudad intermedia, en este caso "Cuenca".

#Evidentemente, en el caso más simple de dos ciudades, la función más rapida es el método de Dijkstra, que ya está incluído en los otros métodos.

#Caso 2: 3 ciudades:

print("\n\nProblema 2: Ruta que pasa por Lugo, Zaragoza y Almería.")

problema2 = ["Lugo", "Zaragoza", "Almería"]

t1 = time.perf_counter()
x, y = resolver_tsp_backtracking(ES, camino_mas_rapido, "Lugo", problema2)
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in x:
    rec= rec + elements + " "

print("\nMétodo TSP Backtracking:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {y}min.")
print(f"   Tiempo tardado: {t}ms")

t1 = time.perf_counter()
x, y = nearest_neighbor_tsp(ES, camino_mas_rapido, "Lugo", problema2)
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in x:
    rec= rec + elements + " "

print("\nMétodo TSP Nearest Neighbor:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {y}min.")
print(f"   Tiempo tardado: {t}ms")

#En este caso, la ruta que calculan es la misma, pero el tiempo de ejecución del método Backtracking es mayor.
#Conclusión: para casos sencillos, el método Nearest Neighbor es mejor.

#Caso 3: 5 ciudades.

problema3 = ["Huelva", "Barcelona", "Ávila", "Pamplona", "Oviedo"]

print("\n\nProblema 3: Ruta que pasa por Huelva, Barcelona, Ávila, Pamplona y Oviedo.")

t1 = time.perf_counter()
x, y = resolver_tsp_backtracking(ES, camino_mas_rapido, "Pamplona", problema3)
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in x:
    rec= rec + elements + " "

print("\nMétodo TSP Backtracking:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {y}min.")
print(f"   Tiempo tardado: {t}ms")

t1 = time.perf_counter()
x, y = nearest_neighbor_tsp(ES, camino_mas_rapido, "Pamplona", problema3)
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in x:
    rec= rec + elements + " "

print("\nMétodo TSP Nearest Neighbor:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {y}min.")
print(f"   Tiempo tardado: {t}ms")

#En este caso sucede lo mismo, el metodo Nearest Neighbor es el más óptimo.

#Caso 4: 10 ciudades

problema4 = ["Albacete", "Gerona", "Teruel", "Vitoria", "Córdoba", "Logroño", "Santander", "Lérida", "Zamora", "Sevilla"]

print("\n\nProblema 2: Ruta que pasa por 10 ciudades.")

t1 = time.perf_counter()
x, y = resolver_tsp_backtracking(ES, camino_mas_rapido, "Vitoria", problema4)
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in x:
    rec= rec + elements + " "

print("\nMétodo TSP Backtracking:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {y}min.")
print(f"   Tiempo tardado: {t}ms")

t1 = time.perf_counter()
x, y = nearest_neighbor_tsp(ES, camino_mas_rapido, "Vitoria", problema4)
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in x:
    rec= rec + elements + " "

print("\nMétodo TSP Nearest Neighbor:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {y}min.")
print(f"   Tiempo tardado: {t}ms")

#Ahora sí, el resultado obtenido en ambos casos es distinto. La ruta calculada por el método backtracking es más rápida que la calculada por Nearest Neighbor. Sin embargo, ha tardado muchísimo más.
#A niveles prácticos, aunque el método de Backtracking sea más acertado ya que comprueba todas las rutas posibles, el tiempo que tarda en calcularlo aumenta de forma n!.
#Según chatgpt, si la ruta a calcular fuera para 15 ciudades, y cada en cada ruta gastara 1ns, en total tardaría 28 días en completarlo. Y sin embargo, con Nearest Neighbor:

print("\nCaso 5: Ruta que pasa por 15 ciudades:")

problema5 = ["Alicante", "Mérida", "Ourense", "Granada", "Soria", "Zamora", "Ciudad Real", "Burgos", "Jaén", "Logroño", "Santander", "Cuenca", "Badajoz", "Toledo", "León"]

t1 = time.perf_counter()
x, y = nearest_neighbor_tsp(ES, camino_mas_rapido, "Alicante", problema5)
t2 = time.perf_counter()
t = (t2-t1)*1000

rec=""
for elements in x:
    rec= rec + elements + " "

print("\nMétodo TSP Nearest Neighbor:")
print(f"   Recorrido: {rec}")
print(f"   Distancia: {y}min.")
print(f"   Tiempo tardado: {t}ms") #No tarda ni 1 segundo.