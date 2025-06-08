## Jonathan Beltran Neri 22310188
## Práctica 5 – Árbol de Mínimo y Máximo Costo con Kruskal (Consola + Gráfico)

import networkx as nx
import matplotlib.pyplot as plt

# Grafo representado como diccionario de aristas: (nodo1, nodo2): peso
grafo = {
    ('Terminal', 'Centro'): 8,
    ('Terminal', 'Tren'): 6,
    ('Centro', 'Taxi'): 5,
    ('Centro', 'Camión'): 7,
    ('Tren', 'Aeropuerto'): 9,
    ('Taxi', 'Camión'): 12,
    ('Aeropuerto', 'Camión'): 15,
    ('Taxi', 'Mercado'): 4,
    ('Camión', 'Mercado'): 6,
    ('Aeropuerto', 'Mercado'): 10
}

# Unión-Find para detectar ciclos en Kruskal
class UnionFind:
    def __init__(self):
        self.padre = {}

    def encontrar(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.encontrar(self.padre[nodo])
        return self.padre[nodo]

    def unir(self, nodo1, nodo2):
        raiz1 = self.encontrar(nodo1)
        raiz2 = self.encontrar(nodo2)
        if raiz1 != raiz2:
            self.padre[raiz2] = raiz1

    def agregar(self, nodo):
        if nodo not in self.padre:
            self.padre[nodo] = nodo

# Algoritmo de Kruskal generalizado para mínimo o máximo costo
def kruskal(grafo, modo='minimo'):
    uf = UnionFind()
    aristas = sorted(grafo.items(), key=lambda x: x[1], reverse=(modo == 'maximo'))
    mst = []
    total = 0

    print(f"\nConstruyendo árbol de {'máximo' if modo == 'maximo' else 'mínimo'} costo con Kruskal:")

    for (nodo1, nodo2), peso in aristas:
        uf.agregar(nodo1)
        uf.agregar(nodo2)
        if uf.encontrar(nodo1) != uf.encontrar(nodo2):
            uf.unir(nodo1, nodo2)
            mst.append((nodo1, nodo2, peso))
            total += peso
            print(f"✔ Arista añadida: {nodo1} — {nodo2} (peso: {peso})")

    print(f"\nÁrbol completado. Costo total: {total}\n")
    return mst

# Gráfica del grafo con resaltado de MST

def graficar_kruskal(grafo, aristas_resaltadas, titulo):
    G = nx.Graph()
    for (n1, n2), peso in grafo.items():
        G.add_edge(n1, n2, weight=peso)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=11)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    aristas_dibujar = [(a, b) for a, b, _ in aristas_resaltadas]
    nx.draw_networkx_edges(G, pos, edgelist=aristas_dibujar, width=3, edge_color='red')

    plt.title(titulo)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Ejecutar Kruskal mínimo
mst_min = kruskal(grafo, modo='minimo')
graficar_kruskal(grafo, mst_min, "Árbol de Mínimo Costo con Kruskal")

# Ejecutar Kruskal máximo
mst_max = kruskal(grafo, modo='maximo')
graficar_kruskal(grafo, mst_max, "Árbol de Máximo Costo con Kruskal")
