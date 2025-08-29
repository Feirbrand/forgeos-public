import networkx as nx
import matplotlib.pyplot as plt

def create_corset_lace_topology(num_eyelet_pairs=8, lace_color='red', eyelet_color='black'):
    """
    Creates a network topology resembling a corset lace pattern.

    Args:
        num_eyelet_pairs (int): The number of eyelet pairs on each side.
        lace_color (str): The color for the lace edges.
        eyelet_color (str): The color for the eyelet edges.

    Returns:
        tuple: A tuple containing the graph, node positions, edge colors,
               and node colors.
    """
    G = nx.Graph()
    pos = {}
    edge_colors = []
    node_colors = []

    # Add eyelet nodes
    for i in range(num_eyelet_pairs):
        # Left side
        G.add_node(f'L{i}')
        pos[f'L{i}'] = (0, i)
        # Right side
        G.add_node(f'R{i}')
        pos[f'R{i}'] = (1, i)
        node_colors.append('gray')
        node_colors.append('gray')


    # Add eyelet edges (the sides of the corset)
    for i in range(num_eyelet_pairs - 1):
        G.add_edge(f'L{i}', f'L{i+1}')
        edge_colors.append(eyelet_color)
        G.add_edge(f'R{i}', f'R{i+1}')
        edge_colors.append(eyelet_color)

    # Add lace edges (the criss-cross pattern)
    for i in range(num_eyelet_pairs - 1):
        G.add_edge(f'L{i}', f'R{i+1}')
        edge_colors.append(lace_color)
        G.add_edge(f'R{i}', f'L{i+1}')
        edge_colors.append(lace_color)

    return G, pos, edge_colors, node_colors


def visualize_topology(G, pos, edge_colors, node_colors):
    """
    Visualizes the network topology.

    Args:
        G (nx.Graph): The graph to visualize.
        pos (dict): A dictionary of node positions.
        edge_colors (list): A list of edge colors.
        node_colors (list): A list of node colors.
    """
    plt.figure(figsize=(6, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=500, font_size=8)
    plt.title("Corset Lace Network Topology")
    plt.show()


def main():
    """
    Main function to create and visualize the topology.
    """
    print("Network Topology Visualizer for Corset Lace Patterns")
    print("Using NetworkX and dummy data only.")
    print("-" * 20)

    # Create the topology
    G, pos, edge_colors, node_colors = create_corset_lace_topology()

    # Visualize the topology
    print("Generating visualization...")
    visualize_topology(G, pos, edge_colors, node_colors)
    print("Visualization displayed.")


if __name__ == "__main__":
    main()
