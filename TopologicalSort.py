### Topological sort code used from recitation ###
### Problem 26 on Rosalind ###

# read pair of numbers
def read_pair(handle):
    line = handle.readline()
    # split string into two parts
    line = line.strip().split()
    # turn string into numbers
    return [int(s) for s in line]

def dfs(u, adj, order, mark):
    mark[u] = True
    for v in adj[u]:
        if not mark[v]:
            dfs(v, adj, order, mark)
    # put verticies in list in order of finishing line
    order.append(u)

# file handling
with open('input.txt') as handle:
    # read number of verticies and edges
    n, m = read_pair(handle)
    # initialize adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = read_pair(handle)
        adj[u-1].append(v-1)
    # output array
    order = []
    # array for markings
    mark = [False] * n
    for u in range(n):
        # call dfs for non-visited vertex u
        if not mark[u]:
            dfs(u, adj, order, mark)
    order.reverse()
    for v in order:
        print(v+1)
