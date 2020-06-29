### Connected Components  ###
### Problem 10 on Rosalind ###
### Hint: DFS ###
### instead of reading from txt file use map() and input() to take input and
### print out the connected components to terminal

# Depth first search: algorithm description on Rosalind problem with pseudocode
def dfs(adj, visited, x):
    # want to assume it is visited
    visited[x] = True
    for y in adj[x]:
        if not visited[y]:
            dfs(adj, visited, y)

# function to give the answer for connected component count 
def connectedComponentAmount(adj):
    totalConnected = 0
    visited = [None] * len(adj)
    # loop through visited nodes
    for z in range(len(visited)):
        if not visited[z]:
            totalConnected += 1
            dfs(adj, visited, z)
    return totalConnected

def connectedComponent():
    # map(): returns map object of result after applying function
    # input(): take user input
    # split(): splits the nodes and edges
    # take in the nodes and edges input 
    nodes, edges = map(int, input().split())
    # store into our adjacent array
    adj = [[] for x in range(nodes)]
    for y in range(edges):
        a1, a2 = map(int, input().split())
        adj[a1-1].append(a2-1)
        adj[a2-1].append(a1-1)
    # print out the answer
    print(connectedComponentAmount(adj))


# run our function to get answer
connectedComponent()


    



