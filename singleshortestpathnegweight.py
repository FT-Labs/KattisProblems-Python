from math import inf

def bellman_ford(N, edges, start):
    dist = [inf] * N
    dist[start] = 0
    for _ in range(N - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    neg = [False] * N
    changes = True
    while changes:
        changes = False
        for u, v, w in edges:
            if not neg[v] and (neg[u] or dist[u] + w < dist[v]):
                neg[v] = changes = True
    return dist, neg


N, M, Q, S = (int(x) for x in input().split())
while N or M or Q or S:
    edges = [tuple(int(x) for x in input().split()) for _ in range(M)]
    dist, neg = bellman_ford(N, edges, S)
    for _ in range(Q):
        q = int(input())
        if neg[q]:
            print ("-Infinity")
        else:
            print (dist[q] if dist[q] != inf else "Impossible")
    print()
    N, M, Q, S = (int(x) for x in input().split())