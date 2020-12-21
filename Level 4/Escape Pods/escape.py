   
#This class represents a directed graph using adjacency matrix representation 
class Graph: 
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self. ROW = len(graph) 

    def BFS(self,s, t, parent):
        visited =[False]*(self.ROW)   
        queue=[]    
        queue.append(s) 
        visited[s] = True      
        while queue: 
            u = queue.pop(0) 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
        return True if visited[t] else False
              
      
    def FordFulkerson(self, source, sink): 
        parent = [-1]*(self.ROW)
        max_flow = 0 
        while self.BFS(source, sink, parent) : 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
            max_flow +=  path_flow 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
        return max_flow 


def solution(entrances, exits, path):
    #The basic idea of this solution is to turn this classic max-flow problem into a single
    #source/sink problem by adding summy sources/sinks with infinite capacities. Once the paths
    #are modified we can use a textbook Ford-Fulkerson algorithm implementation to find out answer
    
    #My first instinct was to just make the new vertex changes directly to the adjacency matrix, however
    #I could also extend the functionality of the Graph class by implementing addVertex and addEdge functions
    inf = float("inf")
    new_exit = exits[0]
    new_entrance = entrances[0]
    dum_source = False
    
    if len(entrances) > 1:
        new_entrance = 0
        dum_source = True
        for i in path:
            i.insert(0,0)
        dummy_source= [0] * (len(path)+1)
        for entrance in entrances:
            dummy_source[entrance + 1] = inf
        path.insert(0, dummy_source)
    
    if len(exits)>1:
        new_exit = len(path)
        for i in path:
            i.append(0)
        for exit in exits:
            if dum_source:
                path[exit+1][len(path)] = inf
            else:
                path[exit][len(path)] = inf

        dummy_sink = [0] * (len(path)+1)
        path.append(dummy_sink)

    g = Graph(path)
 
    return g.FordFulkerson(new_entrance, new_exit)
    
    
test1 = [[0, 7, 0, 0],
         [0, 0, 6, 0], 
         [0, 0, 0, 8], 
         [9, 0, 0, 0]]

test2 = [[0, 0, 4, 6, 0, 0], 
         [0, 0, 5, 2, 0, 0], 
         [0, 0, 0, 0, 4, 4], 
         [0, 0, 0, 0, 6, 6], 
         [0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0]]

gfg1 = [[0,16,13,0,0,0],
        [0,0,10,12,0,0],
        [0,4,0,0,14,0],
        [0,0,9,0,0,20],
        [0,0,0,7,0,4],
        [0,0,0,0,0,0]]

somewhere = [[0, 10, 8, 0, 0, 0],
             [0, 0, 5, 5, 0, 0],
             [0, 4, 0, 0, 10, 0],
             [0, 0, 9, 0, 10, 3],
             [0, 0, 0, 6, 0, 14],
             [0, 0, 0, 0, 0, 0]]

print "Should be 6, results: ", solution([0], [3], test1)
print "Should be 16, results: ",solution([0,1], [4, 5], test2)
print "Should be 23, results: ",solution([0], [5], gfg1)
print "Should be 15, results: ",solution([0], [5], somewhere)



