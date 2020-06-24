import heapq

def dijkstra(adj, start):
    q = [(0, start)]
    dists = {}
    while q:
        d, u = heapq.heappop(q)
        if u in dists:
            continue
        dists[u] = d
        for v, w in adj[u]:
            if v not in dists:
                heapq.heappush(q, (d + w, v))

    return dists

N , M , Q , S = [int(x) for x in input().split(" ")]

while any([N,M,Q,S]) != 0:
    dist = [[] for _ in range(N)]

    for i in range(M):
        u,v,w = input().split()
        dist[int(u)].append((int(v),int(w)))
    paths = dijkstra(dist,S)
    for _ in range(Q):
        q = int(input())
        print(paths[q] if q in paths else "Impossible")
    print()
    N, M, Q, S = [int(x) for x in input().split()]