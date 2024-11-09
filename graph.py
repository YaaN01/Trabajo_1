#Aquí está el grafo con las capitales de provincias de España y el tiempo que se tarda entre ellas
import networkx as nx
import matplotlib.pyplot as plt

#Lista de ciudades:
capitales_provincia = [
    "A Coruña", "Albacete", "Alicante", "Almería", "Ávila", "Badajoz", "Barcelona", "Bilbao", "Burgos", "Cáceres", "Cádiz",
    "Castellón de la Plana", "Ciudad Real", "Córdoba", "Cuenca", "Gerona", "Granada", "Guadalajara", "Huelva", "Huesca", "Jaén", "León",
    "Lérida", "Logroño", "Lugo", "Madrid", "Málaga", "Mérida", "Murcia", "Ourense", "Oviedo", "Palencia", "Pamplona", "Pontevedra",
    "Salamanca", "San Sebastián", "Santander", "Santiago", "Segovia", "Sevilla", "Soria", "Tarragona", "Teruel", "Toledo", "Valencia",
    "Valladolid", "Vitoria", "Zamora", "Zaragoza"
]

ES = nx.Graph()

#Añadimos las ciudades como nodos:
for x in capitales_provincia:
    ES.add_node(x)

#Lista de adyacencia con los tiempos de viaje entre ciudades:
tiempos_viaje = {
    ("A Coruña", "Lugo"): 68,
    ("A Coruña", "Santiago"): 48,
    ("Albacete", "Alicante"): 105,
    ("Albacete", "Ciudad Real"): 136,
    ("Albacete", "Cuenca"): 115,
    ("Albacete", "Jaén"): 184,
    ("Albacete", "Murcia"): 89,
    ("Albacete", "Valencia"): 136,
    ("Alicante", "Murcia"): 56,
    ("Alicante", "Valencia"): 118,
    ("Almería", "Granada"): 103,
    ("Almería", "Jaén"): 133,
    ("Almería", "Murcia"): 132,
    ("Ávila", "Cáceres"): 160,
    ("Ávila", "Madrid"): 74,
    ("Ávila", "Salamanca"): 65,
    ("Ávila", "Segovia"): 53,
    ("Ávila", "Toledo"): 106,
    ("Ávila", "Valladolid"): 91,
    ("Badajoz", "Cáceres"): 74,
    ("Badajoz", "Huelva"): 187,
    ("Badajoz", "Mérida"): 57,
    ("Badajoz", "Sevilla"): 144,
    ("Barcelona", "Gerona"): 76,
    ("Barcelona", "Lérida"): 115,
    ("Barcelona", "Tarragona"): 72,
    ("Bilbao", "San Sebastián"): 73,
    ("Bilbao", "Santander"): 68,
    ("Bilbao", "Vitoria"): 49,
    ("Burgos", "León"): 103,
    ("Burgos", "Logroño"): 88,
    ("Burgos", "Palencia"): 58,
    ("Burgos", "Santander"): 119,
    ("Burgos", "Segovia"): 138,
    ("Burgos", "Soria"): 107,
    ("Burgos", "Valladolid"): 81,
    ("Burgos", "Vitoria"): 74,
    ("Cáceres", "Ciudad Real"): 219,
    ("Cáceres", "Mérida"): 53,
    ("Cáceres", "Salamanca"): 148,
    ("Cáceres", "Toledo"): 150,
    ("Cádiz", "Huelva"): 130,
    ("Cádiz", "Málaga"): 151,
    ("Cádiz", "Sevilla"): 77,
    ("Castellón de la Plana", "Tarragona"): 115,
    ("Castellón de la Plana", "Teruel"): 95,
    ("Castellón de la Plana", "Valencia"): 53,
    ("Ciudad Real", "Córdoba"): 137,
    ("Ciudad Real", "Cuenca"): 157,
    ("Ciudad Real", "Jaén"): 113,
    ("Ciudad Real", "Mérida"): 189,
    ("Ciudad Real", "Toledo"): 83,
    ("Córdoba", "Granada"): 137,
    ("Córdoba", "Jaén"): 81,
    ("Córdoba", "Málaga"): 107,
    ("Córdoba", "Mérida"): 169,
    ("Córdoba", "Sevilla"): 95,
    ("Cuenca", "Guadalajara"): 102,
    ("Cuenca", "Madrid"): 105,
    ("Cuenca", "Teruel"): 128,
    ("Cuenca", "Toledo"): 110,
    ("Cuenca", "Valencia"): 138,
    ("Gerona", "Lérida"): 155,
    ("Granada", "Jaén"): 60,
    ("Granada", "Málaga"): 82,
    ("Guadalajara", "Madrid"): 49,
    ("Guadalajara", "Segovia"): 93,
    ("Guadalajara", "Soria"): 106,
    ("Guadalajara", "Teruel"): 164,
    ("Guadalajara", "Zaragoza"): 164,
    ("Huelva", "Sevilla"): 63,
    ("Huesca", "Lérida"): 76,
    ("Huesca", "Pamplona"): 135,
    ("Huesca", "Zaragoza"): 51,
    ("Jaén", "Murcia"): 212,
    ("León", "Lugo"): 176,
    ("León", "Ourense"): 178,
    ("León", "Oviedo"): 88,
    ("León", "Palencia"): 88,
    ("León", "Santander"): 159,
    ("León", "Valladolid"): 110,
    ("León", "Zamora"): 91,
    ("Lérida", "Tarragona"): 68,
    ("Lérida", "Zaragoza"): 96,
    ("Logroño", "Pamplona"): 58,
    ("Logroño", "Soria"): 83,
    ("Logroño", "Vitoria"): 68,
    ("Lugo", "Ourense"): 84,
    ("Lugo", "Oviedo"): 155,
    ("Lugo", "Santiago"): 75,
    ("Madrid", "Segovia"): 64,
    ("Madrid", "Toledo"): 54,
    ("Málaga", "Sevilla"): 141,
    ("Mérida", "Sevilla"): 115,
    ("Ourense", "Pontevedra"): 83,
    ("Ourense", "Santiago"): 66,
    ("Oviedo", "Santander"): 120,
    ("Palencia", "Valladolid"): 38,
    ("Pamplona", "San Sebastián"): 66,
    ("Pamplona", "Soria"): 126,
    ("Pamplona", "Vitoria"): 68,
    ("Pamplona", "Zaragoza"): 117,
    ("Pontevedra", "Santiago"): 46,
    ("Salamanca", "Valladolid"): 75,
    ("Salamanca", "Zamora"): 45,
    ("San Sebastián", "Vitoria"): 72,
    ("Segovia", "Soria"): 140,
    ("Segovia", "Valladolid"): 80,
    ("Soria", "Zaragoza"): 117,
    ("Tarragona", "Teruel"): 211,
    ("Tarragona", "Zaragoza"): 148,
    ("Teruel", "Valencia"): 89,
    ("Teruel", "Zaragoza"): 112,
    ("Valladolid", "Zamora"): 70
}

# Añadimos las aristas con los pesos:
for (ciudad_1, ciudad_2), tiempo in tiempos_viaje.items():
    ES.add_edge(ciudad_1, ciudad_2, weight=tiempo)

# Se le dan coordenadas a las ciudades para la representación posterior:
coordenadas = {
    "A Coruña": (43.3623, -8.4115), "Albacete": (38.994, -1.8585), "Alicante": (38.3452, -0.4815),
    "Almería": (36.8381, -2.4637), "Ávila": (40.6563, -4.7472), "Badajoz": (38.8794, -6.9707), "Barcelona": (41.3851, 2.1734),
    "Bilbao": (43.2630, -2.9350), "Burgos": (42.3417, -3.7038), "Cáceres": (39.4765, -6.3729), "Cádiz": (36.5271, -6.2886),
    "Castellón de la Plana": (39.9834, -0.0499), "Ciudad Real": (38.9867, -3.9270), "Córdoba": (37.8882, -4.7794),
    "Cuenca": (40.0714, -2.1374), "Gerona": (41.9794, 2.8214), "Granada": (37.1773, -3.5986), "Guadalajara": (40.6343, -3.1645),
    "Huelva": (37.2614, -6.9497), "Huesca": (42.1401, -0.4080), "Jaén": (37.7791, -3.7797), "León": (42.5987, -5.5671),
    "Lérida": (41.6222, 0.6224), "Logroño": (42.4687, -2.4453), "Lugo": (43.0089, -7.5574), "Madrid": (40.4168, -3.7038),
    "Málaga": (36.7213, -4.4217), "Mérida": (38.9164, -6.3432), "Murcia": (37.9833, -1.1307), "Ourense": (42.3364, -7.8681),
    "Oviedo": (43.3619, -5.8494), "Palencia": (42.0097, -4.5269), "Pamplona": (42.8125, -1.6458), "Pontevedra": (42.4333, -8.6486),
    "Salamanca": (40.9704, -5.6635), "San Sebastián": (43.3183, -1.9812), "Santander": (43.4623, -3.8099), "Santiago": (42.8782, -8.5448),
    "Segovia": (40.9481, -4.1075), "Sevilla": (37.3886, -5.9823), "Soria": (41.7632, -2.4676), "Tarragona": (41.1189, 1.2445),
    "Teruel": (40.3455, -1.1067), "Toledo": (39.8628, -4.0273), "Valencia": (39.4699, -0.3763), "Valladolid": (41.6522, -4.7237),
    "Vitoria": (42.8500, -2.6700), "Zamora": (41.5034, -5.7490), "Zaragoza": (41.6488, -0.8891)
}


# Visualización del grafo
"""plt.figure(figsize=(12, 12))
pos = {ciudad: (coordenadas[ciudad][1], coordenadas[ciudad][0]) for ciudad in capitales_provincia}
nx.draw(ES, pos, with_labels=True, node_color='lightgray', node_size=1500, font_size=8)
edge_labels = nx.get_edge_attributes(ES, 'weight')
nx.draw_networkx_edge_labels(ES, pos, edge_labels=edge_labels, font_size=8)
plt.title('Red de Carreteras entre las Capitales de Provincias de España', fontsize=14)
plt.show()"""