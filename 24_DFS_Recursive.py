def dfs_recursive(graph, start, visited=None): 
    #Visited is optional and initialized to None so that it can be set as an empty set on the first call.
    
    if visited is None: #This condition avoids infinite loops
    visited = set()
    
    visited.add(start)
    
    #In the below step, the node undergoes processing and the print function can be replaced by any
    # other task to be done
    print(start, end = " ")
    
    for neighbour in graph[start]:
        
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)
    
    return visited

# Create an adjacency list for the graph
graph = {
    0 : [1, 2],
    1 : [0, 3, 4],
    2 : [0],
    3 : [1],
    4 : [1]
}

dfs_recursive(graph, 0)
