from math import radians, sin, cos, sqrt, atan2

"""
Primero usamos Google maps para buscar las coordenadas de cada parada de metro
"""
LISTA_COORDENADAS = {
    "LINEA_A": {
        "Alberti": [-34.60979154021843, -58.40086740463643],
        "Pasco": [-34.609455989895245, -58.39833539938651],
        "Congreso": [-34.608996813572965, -58.39268130286541],
        "Sáenz Peña": [-34.609350026351635, -58.38669461230903],
        "Lima": [-34.60904096524644, -58.382553281561165], #TRANSBORDO 3
        "Avenida de mayo": [-34.608952661864095, -58.380707921841704],
        "Piedras": [-34.60886435838594, -58.37861579874318],
        "Perú": [-34.60857295624564, -58.37492507907565], #TRANSBORDO 2
        "Plaza de Mayo": [-34.60875839408815, -58.37151330936176],
       
    },
    "LINEA_B": {
        "Pasteur": [-34.60409382222638, -58.39968610352264],
        "Callao": [-34.60434108592872, -58.39243341083207],
        "Uruguay": [-34.60400961150244, -58.38674150304544],
        "Carlos Pellegrini": [-34.60370936151744, -58.381380708823514], #TRANSBORDO 4
        "Lavalle Florida": [-34.603244782294965, -58.37454489610343],
        "Leandro N. Alem": [-34.60302925135683, -58.37004749037363],
    },
    "LINEA_C": {
        "Constitución": [-34.62753942668646, -58.38156121435256],
        "San Juan": [-34.622153370728164, -58.37994066311232],
        "Independencia": [-34.6180519466846, -58.380256098860485], #TRANSBORDO 1
        "Moreno": [-34.61237244698663, -58.38060876062811],
        "Avenida de Mayo": [-34.60899098423044, -58.38066790483753], #TRANSBORDO 3
        "Diagonal Norte": [-34.60482400192541, -58.379488963667214], #TRANSBORDO 4
        "Lavalle": [-34.60207510706261, -58.37814441867528],
        "General San Martin": [-34.59553840845914, -58.37745834587982],
        "Retiro": [-34.59238671801715, -58.37594819705223]
    },
    "LINEA_D": {
        "Facultad de Medicina": [-34.5993682836706, -58.3977359491304],
        "Callao": [-34.59957140474557, -58.392307158181815],
        "Tribunales": [-34.60176154833913, -58.38456093858365],
        "9 de Julio": [-34.60453888530524, -58.38014065809253], #TRANSBORDO 4
        "Diagonal Norte": [-34.60486562472501, -58.37949692792799],
        "catedral": [-34.60757221396939, -58.37419688300631] #TRANSBORDO 2
    },
    "LINEA_E": {
        "Pichincha": [-34.62304099718662, -58.39710097116426],
        "Entre Ríos": [-34.62270550042393, -58.391489789929345],
        "San José": [-34.62224639739259, -58.385224149714155],
        "Independencia": [-34.61812318513492, -58.380224512115895], #TRANSBORDO 1
        "Belgrado": [-34.6128518852584, -58.37787489702144],
        "Bolivar": [-34.60961123829135, -58.37401251606132] #TRANSBORDO 2
    }
}
transbordos = ["Independencia","Bolívar","Lima","Diagonal"]


"""
Una vez tenemos las coordenadas vamos a aplicar la fórmula de Haversine que nos permite
calcular la distancia entre dos puntos geográficos
"""

def haversine(lat1, lon1, lat2, lon2):
    R = 6371e3  # Radio de la Tierra en metros
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

conexiones = []
# Recorrer cada línea y calcular distancias entre estaciones consecutivas
for linea, estaciones in LISTA_COORDENADAS.items():
    estaciones_nombres = list(estaciones.keys())
    for i in range(len(estaciones_nombres) - 1):
        estacion1 = estaciones_nombres[i]
        estacion2 = estaciones_nombres[i + 1]
        coord1 = estaciones[estacion1]  # Coordenadas de la primera estación
        coord2 = estaciones[estacion2]  # Coordenadas de la segunda estación
        # Calcular la distancia entre estaciones consecutivas
        distancia = haversine(coord1[0], coord1[1], coord2[0], coord2[1])
        # Añadir a la lista de conexiones
        conexiones.append((estacion1, estacion2, distancia))

# Mostrar las conexiones calculadas
for conexion in conexiones:
    print(f"{conexion[0]} -> {conexion[1]}: {conexion[2]:.2f}")

