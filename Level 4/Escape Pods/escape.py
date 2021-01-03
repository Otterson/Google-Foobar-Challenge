from collections import deque
#This class represents a directed graph using adjacency matrix representation 

inf = float("inf")


class Graph: 
    # def __init__(self,graph): 
    #     self.graph = graph 
    #     self. ROW = len(graph) 
    def __init__(self, entrances, exits, path):
        self.graph = [list(row) for row in path]
        self.nodes_number = len(self.graph)
        self.max_flow = None

        self.entrance = self.nodes_number
        self.exit = self.nodes_number + 1

        for row in xrange(self.nodes_number):
            self.graph[row].append(0)
            self.graph[row].append(inf if row in exits else 0)

        self.nodes_number += 2

        self.graph.append([(inf if x in entrances else 0) for x in xrange(self.nodes_number)])
        self.graph.append([0] * self.nodes_number)

    def BFS(self,s, t, parent):
        visited =[False]*len(self.graph)   
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
              
      
    def FordFulkerson(self): 
        parent = [-1]*len(self.graph)
        max_flow = 0 
        while self.BFS(self.entrance, self.exit, parent) : 
            path_flow = float("Inf") 
            s = self.exit 
            
            while(s !=  self.entrance): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
            max_flow +=  path_flow 
            v = self.exit
            while(v !=  self.entrance): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
        return max_flow 
        # max_flow = 0
        # while True:
        #     bfs_path = self.BFS(source, sink)

        #     if bfs_path is None:
        #         break

        #     flow = float("inf")
        #     for i in range(1, len(bfs_path)):
        #         src = bfs_path[i - 1]
        #         dst = bfs_path[i]
        #         flow = min(flow, self.graph[src][dst])

        #     for i in range(1, len(bfs_path)):
        #         src = bfs_path[i - 1]
        #         dst = bfs_path[i]
        #         self.graph[src][dst] -= flow
        #         self.graph[dst][src] += flow

        #     max_flow += flow

      

        # return max_flow

#---------------------------SOLUTION-----------------------------------------------------

def solution(entrances, exits, path):
    #The basic idea of this solution is to turn this classic max-flow problem into a single
    #source/sink problem by adding summy sources/sinks with infinite capacities. Once the paths
    #are modified we can use a textbook Ford-Fulkerson algorithm implementation to find the answer
    
    #My first instinct was to just make the new vertex changes directly to the adjacency matrix, however
    #I could also extend the functionality of the Graph class by implementing addVertex and addEdge functions
    inf = float("inf")
    

    g = Graph(entrances, exits,path)
    for i in path:
        print i
    
    # return g.FordFulkerson(new_entrance, new_exit)
    return g.FordFulkerson()




#-----------------------TEST CASES--------------------------------------------------
          
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



print "Should be 6, results: \n", solution([0], [2,3], test1)
print "\n\n"
print "Should be 16, results: \n",solution([0,1], [4, 5], test2)
print "\n\n"
print "Should be 23, results: \n",solution([0], [5], gfg1)
print "\n\n"
print "Should be 15, results: \n",solution([0], [5], somewhere)

print "\n\n"



