import networkx as nx
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, atan2

# Grafo
G = nx.Graph()

# Función Haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371e3  # Radio de la Tierra en metros
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Función para calcular la distancia entre dos coordenadas
def distancia(coordenadas_1, coordenadas_2) -> float:
    return haversine(coordenadas_1[0], coordenadas_1[1], coordenadas_2[0], coordenadas_2[1])

# Coordenadas de las estaciones
LISTA_COORDENADAS = {
    "LINEA_A": {
        "Alberti": [-34.60979154021843, -58.40086740463643],
        "Pasco": [-34.609455989895245, -58.39833539938651],
        "Congreso": [-34.608996813572965, -58.39268130286541],
        "Sáenz Peña": [-34.609350026351635, -58.38669461230903],
        "Lima": [-34.60904096524644, -58.382553281561165],
        "Piedras": [-34.60886435838594, -58.37861579874318],
        "Perú": [-34.60857295624564, -58.37492507907565],
        "Plaza de Mayo": [-34.60875839408815, -58.37151330936176],
    },
    "LINEA_B": {
        "Pasteur": [-34.60409382222638, -58.39968610352264],
        "Callao_B": [-34.60434108592872, -58.39243341083207],
        "Uruguay": [-34.60400961150244, -58.38674150304544],
        "Carlos Pellegrini": [-34.60370936151744, -58.381380708823514],
        "Florida": [-34.603244782294965, -58.37454489610343],
        "Leandro N. Alem": [-34.60302925135683, -58.37004749037363],
    },
    "LINEA_C": {
        "Constitución": [-34.62753942668646, -58.38156121435256],
        "San Juan": [-34.622153370728164, -58.37994066311232],
        "Independencia_C": [-34.6180519466846, -58.380256098860485],
        "Moreno": [-34.61237244698663, -58.38060876062811],
        "Avenida de Mayo": [-34.60899098423044, -58.38066790483753],
        "Diagonal Norte": [-34.60482400192541, -58.379488963667214],
        "Lavalle": [-34.60207510706261, -58.37814441867528],
        "General San Martin": [-34.59553840845914, -58.37745834587982],
        "Retiro": [-34.59238671801715, -58.37594819705223],
    },
    "LINEA_D": {
        "Facultad de Medicina": [-34.5993682836706, -58.3977359491304],
        "Callao_D": [-34.59957140474557, -58.392307158181815],
        "Tribunales": [-34.60176154833913, -58.38456093858365],
        "9 de Julio": [-34.60453888530524, -58.38014065809253],
        "Catedral": [-34.60757221396939, -58.37419688300631],
    },
    "LINEA_E": {
        "Pichincha": [-34.62304099718662, -58.39710097116426],
        "Entre Ríos": [-34.62270550042393, -58.391489789929345],
        "San José": [-34.62224639739259, -58.385224149714155],
        "Independencia_E": [-34.61812318513492, -58.380224512115895],
        "Belgrano": [-34.6128518852584, -58.37787489702144],
        "Bolivar": [-34.60961123829135, -58.37401251606132],
    },
}

# Agregamos nodos con posiciones
for linea, estaciones in LISTA_COORDENADAS.items():
    for estacion, coordenadas in estaciones.items():
        G.add_node(estacion, pos=coordenadas)

# Definimos las distancias entre las estaciones
for linea, estaciones in LISTA_COORDENADAS.items():
    estaciones_lista = list(estaciones.keys())
    for i in range(len(estaciones_lista) - 1):
        estacion1 = estaciones_lista[i]
        estacion2 = estaciones_lista[i + 1]
        coord1 = estaciones[estacion1]
        coord2 = estaciones[estacion2]
        G.add_edge(estacion1, estacion2, weight=distancia(coord1, coord2))

# Obtener posiciones de los nodos
pos = nx.get_node_attributes(G, 'pos')

# Lista de transbordos con las conexiones manuales
transbordos = [
    ("Lima", "Avenida de Mayo"),  # Línea A <-> Línea C
    ("Perú", "Catedral"),         # Línea A <-> Línea D
    ("Independencia", "Independencia"),  # Línea C <-> Línea E
    ("Bolivar", "Perú"),          # Línea E <-> Línea A
    ("Diagonal Norte", "Carlos Pellegrini"),  # Línea C <-> Línea B
    ("Carlos Pellegrini", "9 de Julio"),      # Línea B <-> Línea D
    ("9 de Julio", "Diagonal Norte"),         # Línea D <-> Línea C
]

# Agregar las aristas entre las estaciones de transbordo
for estacion1, estacion2 in transbordos:
    if estacion1 in G.nodes and estacion2 in G.nodes:
        G.add_edge(estacion1, estacion2, weight=0)  # Peso a definir




# Función para colorear los nodos según la línea a la que pertenecen
# Agregamos los nodos y las aristas a G
LINEA_A = {"Alberti","Pasco","Congreso","Sáenz Peña","Lima","Piedras", "Perú","Plaza de Mayo"}
LINEA_B = {"Pasteur","Callao","Uruguay","Carlos Pellegrini","Florida","Leandro N. Alem"}
LINEA_C = {"Constitución","San Juan","Independencia","Moreno","Avenida de Mayo","Diagonal Norte","Lavalle","General San Martin","Retiro"}
LINEA_D = {"Facultad de Medicina","Callao","Tribunales","9 de Julio", "Diagonal Norte","Catedral"}
LINEA_E = {"Pichincha","Entre Ríos","San José","Independencia","Belgrano","Bolívar"}
transbordos = {"Lima", "Carlos Pellegrini", "Diagonal Norte", "Bolivar", "Avenida de Mayo", "Retiro"}

def colorear_nodos(G):
    color = []
    estaciones_linea = [transbordos, LINEA_A, LINEA_B, LINEA_C, LINEA_D, LINEA_E]

    for node in G.nodes:
        if node in estaciones_linea[0]:
            color.append('black')
        elif node in estaciones_linea[1]:
            color.append('lightblue')
        elif node in estaciones_linea[2]:
            color.append('red')
        elif node in estaciones_linea[3]:
            color.append('darkblue')
        elif node in estaciones_linea[4]:
            color.append('green')
        elif node in estaciones_linea[5]:
            color.append('purple')
        else:
            color.append('gray')  # Color por defecto si no se encuentra en ninguna línea
    return color


# Función para colorear las aristas
def colorear_edges(G):
    color_edge = []
    estaciones_linea = [transbordos, LINEA_A, LINEA_B, LINEA_C, LINEA_D, LINEA_E]

    for edge in G.edges:
        if edge[0] in estaciones_linea[0] or edge[1] in estaciones_linea[0]:
            color_edge.append('black')
        elif edge[0] in estaciones_linea[1] or edge[1] in estaciones_linea[1]:
            color_edge.append('lightblue')
        elif edge[0] in estaciones_linea[2] or edge[1] in estaciones_linea[2]:
            color_edge.append('red')
        elif edge[0] in estaciones_linea[3] or edge[1] in estaciones_linea[3]:
            color_edge.append('darkblue')
        elif edge[0] in estaciones_linea[4] or edge[1] in estaciones_linea[4]:
            color_edge.append('green')
        elif edge[0] in estaciones_linea[5] or edge[1] in estaciones_linea[5]:
            color_edge.append('purple')
        else:
            color_edge.append('gray')  # Color por defecto
    return color_edge




# Dibujar el grafo
# Coloreamos los nodos y las aristas
node_colors = colorear_nodos(G)
edge_colors = colorear_edges(G)

# Dibujar el grafo
plt.figure(figsize=(12, 10))

# Dibujamos las aristas
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)

# Dibujamos los nodos
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)

# Dibujamos las etiquetas
nx.draw_networkx_labels(G, pos, font_size=12)

plt.show()

