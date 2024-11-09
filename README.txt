Instrucciones:

Hay 3 archivos
-graph.py : Aquí está el grafo con las capitales de provincia de la península, usando networkx. Al final, entre """, hay una representación visual del grafo usando networkx.
-utils.py : Aquí están los métodos para optimizar rutas.
              -camino_mas_rapido : calcula la ruta más rapida, o corta, entre dos ciudades, usando el método de Dijkstra.
              -backtracking_tsp : es la función recursiva que aparece en el siguiente método. No se usa de por sí sola.
              -resolver_tps_backtracking : calcula la ruta más rápida por backtracking.
              -nearest_neighbor_tsp : calcula la ruta más rápida por nearest neighbor.
            Como se ve en el código, tanto backtracking como nearest neighbor, ambos usan Dijkstra para calcular distancias.
-analisis.py : Aquí hago un analisis de la eficacia de los métodos, comparando resultados y tiempos de ejecución.


Instrucciones de uso:
  - camino_mas_rapido(G, ciudad1, ciudad2)
            'G' es el grafo con todos los nodos, y sobre el que se van a hacer todos los cálculos. En nuestro caso, el grafo definido de España se llama ES.
            'ciudad1' ha de ser un string con el nombre de la ciudad inicial.
            'ciudad2' ha de ser un string con el nombre de la ciudad final.
            Al final te devuelve dos valores, una lista con las ciudades recorridas y el tiempo total.

  - resolver_tps_backtracking(G, camino_mas_rapido, ciudad_inicial, ciudades)
            'G' igual que antes, el grafo con las ciudades.
            'camino_mas_rapido' aquí se introduce la función con el método de Dijkstra, en nuestro caso "camino_mas_rapido", para que la propia funcion la pueda utilizar.
            'ciudad_inicial' ha de ser un string con el nombre de la ciudad inicial.
            'ciudades' ha de ser una lista con todas las ciudades a recorrer, incluida o no la ciudad inicial.
            Al final te devuelve dos valores, el tiempo total, y una lista con el orden de las ciudades recorridas, sin incluir las ciudades intermedias no incluidas en la lista "ciudades".
 
  - nearest_neighbor_tsp(G, camino_mas_rapido, ciudad_inicial, ciudades)
            Lo mismo que la función anterior.


El método backtracking calcula TODAS las rutas posibles para encontrar la mejor, mientras que el método Nearest Neighbor busca la ciudad más cercana a la actual, sin tener encuenta todas las ciudades y rutas posibles.
Esto significa que la complejidad de backtracking es muy grande (n!) y por lo tanto es inviable para grafos o rutas grandes.