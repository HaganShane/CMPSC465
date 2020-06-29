### Bellman Ford Algorithm on page 118 ###
### Problem 22 on Rosalind ###
### use map(), similar to connected components w/ nodes and edges

# function to read the given graph w/ user input
def graph():
    # read user input (copy / paste set from
    # almost same as connected components problem
    # take in the graph and read the inputs / assign to variables needed
    nodes, edges = map(int, input().split())
    graphEdges = []
    for x in range(edges):
        a1, a2, edgeWeight = map(int, input().split())
        graphEdges.append((a1 - 1, a2 - 1, edgeWeight))
    return nodes, graphEdges

def distance(nodes, graphEdges):
    '''
    dist(s)=0
    repeat |V|-1 times
    for all e in E
        update(e)
    '''
    # initialize dist and dist[0] 
    dist = [None] * nodes
    dist[0] = 0

    # repeat |v| - 1 times
    for x in range(nodes - 1):
        # for all e in E
        for v1, v2, edgeWeight in graphEdges:
            # update (e)
            if dist[v1] != None and (dist[v2] == None or dist[v2] > dist[v1] + edgeWeight):
                dist[v2] = dist[v1] + edgeWeight
    return dist

# call this main bellman ford function
def bellmanFord():
    # print the distance, otherwise put an x if there is none
    # main output to terminal
    print(' '.join(map(lambda x: str(x) if x != None else 'x', distance(*graph()))))

# call bellman ford to run    
bellmanFord()

# worked with sample, try downloading and completing problem
    
