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
        # Añadir la ciudad actual a la ruta
        ruta_actual.append(ciudad)
        
        # Si la ruta tiene más de una ciudad, calculamos el camino más rápido entre la última ciudad y la nueva ciudad
        if len(ruta_actual) > 1:
            distancia, _ = camino_mas_rapido(G, ruta_actual[-2], ruta_actual[-1])
            nueva_distancia = distancia_total + distancia
        else:
            nueva_distancia = 0
        
        # Si la nueva distancia es peor que la mejor ruta encontrada, descartamos este camino
        if nueva_distancia >= mejor_distancia:
            ruta_actual.pop()  # Descartamos la ciudad actual si no es la mejor ruta
            continue
        
        # Actualizamos las ciudades restantes
        nuevas_ciudades_restantes = ciudades_restantes.copy()
        nuevas_ciudades_restantes.remove(ciudad)
        
        # Llamamos recursivamente para continuar con la búsqueda
        mejor_ruta, mejor_distancia = backtracking_tsp(G, camino_mas_rapido, ciudad_inicial, nuevas_ciudades_restantes, ruta_actual, nueva_distancia, mejor_ruta, mejor_distancia)
        
        # Deshacemos el paso actual y continuamos con otro
        ruta_actual.pop()

    # Si ya no quedan ciudades por visitar
    if not ciudades_restantes:
        # Calcular la distancia de vuelta a la ciudad inicial
        distancia, _ = camino_mas_rapido(G, ruta_actual[-1], ciudad_inicial)
        distancia_total += distancia
        
        # Si esta ruta es la mejor encontrada, la guardamos
        if distancia_total < mejor_distancia:
            mejor_distancia = distancia_total
            mejor_ruta = ruta_actual[:]  # Hacemos una copia de la ruta actual (sin la ciudad inicial duplicada)

        return mejor_ruta, mejor_distancia
    
    return mejor_ruta, mejor_distancia

# Función principal que resuelve el TSP usando backtracking
def resolver_tsp_backtracking(G, camino_mas_rapido, ciudad_inicial, ciudades):
    # Inicializamos las ciudades restantes (sin la ciudad inicial)
    ciudades_restantes = [ciudad for ciudad in ciudades if ciudad != ciudad_inicial]
    mejor_ruta = []
    mejor_distancia = float('inf')  # Empezamos con una distancia infinita como la mejor
    
    # Llamamos al método de backtracking para obtener la mejor ruta
    mejor_ruta, mejor_distancia = backtracking_tsp(G, camino_mas_rapido, ciudad_inicial, ciudades_restantes, [ciudad_inicial], 0, mejor_ruta, mejor_distancia)

    # Añadimos la ciudad inicial al final de la ruta (esto no duplicará la ciudad inicial)
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
        
        # Buscar la ciudad más cercana
        for ciudad in ciudades_restantes:
            # Usamos la función camino_mas_rapido para obtener la distancia entre la ciudad actual y la ciudad candidata
            distancia, _ = camino_mas_rapido(G, ciudad_actual, ciudad)
            
            if distancia < distancia_minima:
                ciudad_cercana = ciudad
                distancia_minima = distancia
        
        # Añadimos la ciudad más cercana a la ruta
        ruta.append(ciudad_cercana)
        distancia_total += distancia_minima
        ciudad_actual = ciudad_cercana
        ciudades_restantes.remove(ciudad_cercana)
    
    # Volver a la ciudad inicial (sin añadir ciudades intermedias en el camino de vuelta)
    distancia, _ = camino_mas_rapido(G, ciudad_actual, ciudad_inicial)
    distancia_total += distancia
    ruta.append(ciudad_inicial)
    
    return ruta, distancia_total

