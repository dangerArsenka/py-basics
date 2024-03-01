#Introduction to programming: Task 3
#Tsadzikidze Arsen, FB-24, 26
print('Introduction to programming: Task 3')
print('Tsadzikidze Arsen, FB-24, 26')
#Реалізувати алгоритм Дейкстра по знаходженню найкоротших шляхів від заданої вершини графа до всіх інших

import heapq
def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

#graph = {
#    'A': {'B': 1, 'C': 4},
#   'B': {'A': 1, 'C': 2},
#    'C': {'A': 4, 'B': 2}
#}

#start_vertex = 'A'

#shortest_distances = dijkstra(graph, start_vertex)

#print(shortest_distances)  # {'A': 0, 'B': 1, 'C': 3}

