## Jonathan Beltran Neri 22310188
## Algoritmo de Dijkstra

import networkx as nx               # Para crear y manejar el grafo
import matplotlib.pyplot as plt    # Para visualizar el grafo
import heapq                       # Para usar cola de prioridad (mínima)

# Función que implementa el algoritmo de Dijkstra paso a paso
def dijkstra_visual(grafo, inicio):
    # Inicializamos las distancias con infinito para todos los nodos
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0  # La distancia del nodo de inicio es 0

    visitados = set()  # Lleva registro de los nodos ya visitados
    cola = [(0, inicio)]  # Cola de prioridad: (distancia, nodo)
    caminos = {}  # Guarda el nodo anterior para cada uno (para reconstruir ruta)

    # Recorremos el grafo hasta vaciar la cola
    while cola:
        # Tomamos el nodo con menor distancia actual
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue  # Si ya fue visitado, lo ignoramos

        visitados.add(nodo_actual)
        print(f"\nVisitando nodo: {nodo_actual}, distancia acumulada: {distancia_actual}")

        # Recorremos cada vecino de este nodo
        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia_actual + peso

            # Si encontramos un camino más corto, actualizamos
            if nueva_distancia < distancias[vecino]:
                print(f"  ↳ Actualizando distancia de {vecino}: {distancias[vecino]} → {nueva_distancia}")
                distancias[vecino] = nueva_distancia
                caminos[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))  # Lo agregamos a la cola para procesarlo

    return distancias, caminos

# Función para graficar el grafo con la ruta más corta destacada
def graficar_dijkstra(grafo, distancias, caminos, inicio, destino_final):
    G = nx.DiGraph()  # Creamos un grafo dirigido (flechas)

    # Añadimos todas las conexiones (aristas) y pesos
    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            G.add_edge(nodo, vecino, weight=peso)

    # Calculamos las posiciones de los nodos en el gráfico
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Tomamos los pesos para mostrarlos

    # Dibujamos nodos, aristas y etiquetas
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=11, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Reconstruimos la ruta más corta desde el destino hacia el inicio
    ruta_corta = []
    actual = destino_final
    while actual in caminos:
        anterior = caminos[actual]
        ruta_corta.insert(0, (anterior, actual))  # Lo insertamos al inicio para formar la ruta ordenada
        actual = anterior

    # Dibujamos esa ruta destacada en rojo
    nx.draw_networkx_edges(G, pos, edgelist=ruta_corta, width=3, edge_color='red')

    # Agregamos una nota explicativa en la parte inferior
    plt.text(0, -1.1,
             f'Ruta más rápida desde {inicio} hasta {destino_final} marcada en rojo\n'
             f'Los números indican el tiempo en minutos.',
             fontsize=10, ha='center', color='gray')

    plt.title(f"Ruta más rápida de {inicio} a {destino_final} con Dijkstra")
    plt.axis('off')  # Quitamos el marco del gráfico
    plt.tight_layout()
    plt.show()

# Definimos el grafo con conexiones y pesos (en minutos)
grafo = {
    'Casa': [('Taxi', 8), ('Camión', 15), ('Tren', 4)],
    'Taxi': [('Escuela', 4)],        # Total: 8 + 4 = 12 min
    'Camión': [('Escuela', 8)],      # Total: 15 + 8 = 23 min
    'Tren': [('Escuela', 4)],        # Total: 4 + 4 = 8 min 
    'Escuela': []
}

# Nodo inicial y destino final
inicio = 'Casa'
destino_final = 'Escuela'

# Ejecutamos el algoritmo y visualizamos la ruta óptima
distancias, caminos = dijkstra_visual(grafo, inicio)
graficar_dijkstra(grafo, distancias, caminos, inicio, destino_final)
