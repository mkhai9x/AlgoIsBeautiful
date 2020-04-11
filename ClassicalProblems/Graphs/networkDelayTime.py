'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), 
where u is the source node, v is the target node, and w is the time it takes for a signal to 
travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? 
If it is impossible, return -1. 
'''


def find_minium_dist(graph, N, dist, visited):
    node = -1
    min_dist = 9999
    for i in range(N):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            node = i
    return node


def shortest_paths(graph, N, dist, visited):
    for i in range(N):
        node = find_minium_dist(graph, N, dist, visited)
        visited[node] = True
        for neighbor in graph[node]['Out']:
            if not visited[neighbor[0]]:
                if dist[neighbor[0]] > dist[node] + neighbor[1]:
                    dist[neighbor[0]] = dist[node] + neighbor[1]


def networkDelayTime(times, N, K):
    MAX = 9999
    # create a graph
    graph = {}
    for i in range(N):
        graph[i] = {
            'Out': []
        }
    for time in times:
        graph[time[0] - 1]['Out'].append((time[1] - 1, time[2]))

    visited = [False]*N
    dist = [MAX]*N
    dist[K-1] = 0
    shortest_paths(graph, N, dist, visited)
    if max(dist) == MAX:
        # It is a unconnect graph
        return -1
    return max(dist)


print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

print(networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 1))
