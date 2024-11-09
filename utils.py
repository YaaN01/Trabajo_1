#aquí se definen los métodos
import networkx as nx

#Cálculo del camino más rápido entre dos ciudades por el método de Dijkstra:
def camino_mas_rapido(G, ciudad1, ciudad2):
    distancia, camino = nx.single_source_dijkstra(G, ciudad1, target=ciudad2, weight='weight')
    return distancia, camino

#Método del Viajante(TSP) por Backtracking:

#Función recursiva backtracking:
def backtracking_tsp(G, camino_mas_rapido, ciudad_inicial, ciudades_restantes, ruta_actual, distancia_total, mejor_ruta, mejor_distancia):
    for ciudad in ciudades_restantes:
        ruta_actual.append(ciudad)
        
        if len(ruta_actual) > 1:
            distancia, _ = camino_mas_rapido(G, ruta_actual[-2], ruta_actual[-1])
            nueva_distancia = distancia_total + distancia
        else:
            nueva_distancia = 0
        
        if nueva_distancia >= mejor_distancia:
            ruta_actual.pop()
            continue
        
        nuevas_ciudades_restantes = ciudades_restantes.copy()
        nuevas_ciudades_restantes.remove(ciudad)
        mejor_ruta, mejor_distancia = backtracking_tsp(G, camino_mas_rapido, ciudad_inicial, nuevas_ciudades_restantes, ruta_actual, nueva_distancia, mejor_ruta, mejor_distancia)
        ruta_actual.pop()

    if not ciudades_restantes:
        distancia, _ = camino_mas_rapido(G, ruta_actual[-1], ciudad_inicial)
        distancia_total += distancia
        if distancia_total < mejor_distancia:
            mejor_distancia = distancia_total
            mejor_ruta = ruta_actual[:]

        return mejor_ruta, mejor_distancia
    
    return mejor_ruta, mejor_distancia

def resolver_tsp_backtracking(G, camino_mas_rapido, ciudad_inicial, ciudades):
    ciudades_restantes = [ciudad for ciudad in ciudades if ciudad != ciudad_inicial]
    mejor_ruta = []
    mejor_distancia = float('inf')
    mejor_ruta, mejor_distancia = backtracking_tsp(G, camino_mas_rapido, ciudad_inicial, ciudades_restantes, [ciudad_inicial], 0, mejor_ruta, mejor_distancia)
    mejor_ruta.append(ciudad_inicial)

    return mejor_ruta, mejor_distancia

#Método del Viajante(TSP) por Nearest Neighbor:
def nearest_neighbor_tsp(G, camino_mas_rapido, ciudad_inicial, ciudades):
    ciudades_restantes = [ciudad for ciudad in ciudades if ciudad != ciudad_inicial]
    ruta = [ciudad_inicial]
    distancia_total = 0
    ciudad_actual = ciudad_inicial
    
    while ciudades_restantes:
        ciudad_cercana = None
        distancia_minima = float('inf')
        
        for ciudad in ciudades_restantes:
            distancia, _ = camino_mas_rapido(G, ciudad_actual, ciudad)
            
            if distancia < distancia_minima:
                ciudad_cercana = ciudad
                distancia_minima = distancia
        
        ruta.append(ciudad_cercana)
        distancia_total += distancia_minima
        ciudad_actual = ciudad_cercana
        ciudades_restantes.remove(ciudad_cercana)
    
    distancia, _ = camino_mas_rapido(G, ciudad_actual, ciudad_inicial)
    distancia_total += distancia
    ruta.append(ciudad_inicial)
    
    return ruta, distancia_total

