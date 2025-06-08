## Jonathan Beltran Neri 22310188
## Práctica 4 – Árbol Parcial Mínimo con Prim (Consola + Gráfico)

import networkx as nx                  # Librería para trabajar con grafos
import matplotlib.pyplot as plt       # Librería para generar gráficas

# Definimos el grafo del sistema de transporte urbano
# Cada nodo representa una estación o punto de conexión (Terminal, Centro, etc.)
# Los pesos representan el costo o tiempo entre estaciones
grafo = {
    'Terminal': {'Taxi': 8, 'Camión': 15, 'Tren': 4},
    'Taxi': {'Centro': 5},
    'Camión': {'Centro': 12},
    'Tren': {'Centro': 6, 'Aeropuerto': 7},
    'Centro': {'Mercado': 3},
    'Aeropuerto': {'Mercado': 10},
    'Mercado': {}  # Nodo final, no tiene salidas
}

# Función que implementa el algoritmo de Prim en consola
def prim_consola(grafo, inicio):
    visitados = set()          # Conjunto de nodos ya agregados al árbol
    aristas_mst = []           # Lista de aristas seleccionadas para el árbol
    total = 0                  # Suma total del costo del árbol

    visitados.add(inicio)      # Empezamos desde el nodo inicial
    print(f"\nIniciando en nodo: {inicio}")

    # Mientras no hayamos conectado todos los nodos
    while len(visitados) < len(grafo):
        menor = None
        peso_menor = float('inf')

        # Buscamos la arista más barata que conecte un nodo visitado con uno no visitado
        for nodo in visitados:
            for vecino, peso in grafo[nodo].items():
                if vecino not in visitados and peso < peso_menor:
                    menor = (nodo, vecino)
                    peso_menor = peso

        if menor is None:
            break  # Si no se encontró ninguna arista válida, el grafo no está totalmente conectado

        nodo1, nodo2 = menor
        visitados.add(nodo2)                        # Marcamos el nodo como visitado
        aristas_mst.append((nodo1, nodo2, peso_menor))  # Guardamos la arista en el árbol mínimo
        total += peso_menor

        # Imprimimos el paso realizado
        print(f"✔ Se agrega arista: {nodo1} — {nodo2} (peso: {peso_menor})")
        print(f"  Nodos visitados: {sorted(visitados)}")

    print(f"\nÁrbol de expansión mínima completado. Costo total: {total}")
    return aristas_mst

# Función para graficar el resultado visual del árbol mínimo
def graficar_prim(grafo, aristas_mst):
    G = nx.Graph()  # Creamos un grafo no dirigido para visualización

    # Añadimos todas las aristas con su peso original al grafo
    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():
            G.add_edge(nodo, vecino, weight=peso)

    # Calculamos posiciones automáticas para cada nodo en el gráfico
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Obtenemos los pesos para mostrarlos

    # Dibujo del grafo completo
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=11)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Dibujo de las aristas del árbol mínimo en rojo
    aristas_rojas = [(a, b) for a, b, _ in aristas_mst]
    nx.draw_networkx_edges(G, pos, edgelist=aristas_rojas, width=3, edge_color='red')

    # Texto explicativo debajo del grafo
    plt.text(0, -1.1, 'Aristas rojas: Árbol Parcial Mínimo generado con Prim',
             fontsize=10, ha='center', color='gray')

    plt.title("Árbol de Expansión Mínima con Prim - Transporte Urbano")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Ejecutamos el algoritmo y mostramos la gráfica
inicio = 'Terminal'
aristas_prim = prim_consola(grafo, inicio)
graficar_prim(grafo, aristas_prim)
