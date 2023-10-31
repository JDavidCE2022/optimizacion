import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos
G.add_node("1")
G.add_node("2")
G.add_node("3")
G.add_node("4")
G.add_node("5")
G.add_node("6")
G.add_node("7")

# Agregar aristas con pesos

# Add edges with capacities
G.add_edge("1", "2", capacity=5)
G.add_edge("1", "3", capacity=6)
G.add_edge("1", "5", capacity=7)
G.add_edge("2", "3", capacity=2)
G.add_edge("3", "2", capacity=2)
G.add_edge("2", "4", capacity=4)
G.add_edge("3", "4", capacity=2)
G.add_edge("3", "5", capacity=3)
G.add_edge("3", "6", capacity=8)
G.add_edge("4", "6", capacity=1)
G.add_edge("6", "4", capacity=1)
G.add_edge("4", "7", capacity=8)
G.add_edge("5", "6", capacity=6)
G.add_edge("6", "7", capacity=7)

source = "1"
sink = "7"

max_flow_value, max_flow_dict = nx.maximum_flow(G, source, sink)

print(max_flow_value)

# Encontrar la ruta que permite la mayor cantidad de vehículos
def find_max_flow_path(G, flow_dict, source, sink):
    path = []
    while source != sink:
        neighbors = G[source]
        for neighbor, attr in neighbors.items():
            if flow_dict[source][neighbor] > 0:
                path.append((source, neighbor))
                source = neighbor
                break
    return path

max_flow_path = find_max_flow_path(G, max_flow_dict, source, sink)
print("Ruta con flujo máximo:", max_flow_path)