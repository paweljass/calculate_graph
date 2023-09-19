import networkx as nx

def load_graphml(file_path):
    return nx.read_graphml(file_path)

def calculate_cost_rate_a(graph):
    total_cost = 0
    for node in graph.nodes(data=True):
        if 'type' in node[1]:
            if node[1]['type'] == 'Cabinet':
                total_cost += 1000
            elif node[1]['type'] == 'Pot':
                total_cost += 100
            elif node[1]['type'] == 'Chamber':
                total_cost += 200
    for edge in graph.edges(data=True):
        if 'type' in edge[2]:
            if edge[2]['type'] == 'verge':
                total_cost += 50 * edge[2]['length']
            elif edge[2]['type'] == 'road':
                total_cost += 100 * edge[2]['length']
    return total_cost

def calculate_cost_rate_b(graph):
    total_cost = 0
    for node, edge in zip(graph.nodes(data=True), graph.edges(data=True)):
        if 'type' in node[1]:
            if node[1]['type'] == 'Cabinet':
                total_cost += 1200
            elif node[1]['type'] == 'Pot':
                total_cost += 20 * edge[2]['length']
            elif node[1]['type'] == 'Chamber':
                total_cost += 200
    for edge in graph.edges(data=True):
        if 'type' in edge[2]:
            if edge[2]['type'] == 'verge':
                total_cost += 40 * edge[2]['length']
            elif edge[2]['type'] == 'road':
                total_cost += 80 * edge[2]['length']
    return total_cost


def main():
    file_path = "problem.graphml"
    graph = load_graphml(file_path)
    print(f"total cost with rate card A -> {calculate_cost_rate_a(graph)}£")
    print(f"total cost with rate card b -> {calculate_cost_rate_b(graph)}£")

if __name__ == "__main__":
    main()