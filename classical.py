import networkx as nx

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    paths = []

    while stack:
        node, path = stack.pop()
        for neighbor in graph.neighbors(node):
            if neighbor not in path:
                if neighbor == goal:
                    paths.append(path + [neighbor])
                else:
                    stack.append((neighbor, path + [neighbor]))

    return paths

def shortest_path_from_dfs(graph, dfs_paths):
    min_dist = float("inf")
    best_path = None

    for path in dfs_paths:
        dist = 0
        for i in range(len(path) - 1):
            dist += graph[path[i]][path[i+1]]["weight"]

        if dist < min_dist:
            min_dist = dist
            best_path = path

    return best_path, min_dist

def dijkstra_shortest_path(graph, source):
    return nx.single_source_dijkstra(graph, source)
