# Prints BFS traversal from a given source vertex

from collections import defaultdict 
# "a defaultdict will have a default value if that key has not been set yet.
# If you didn't use a defaultdict you'd have to check to see if that key exists,
# and if it doesn't, set it to what you want."

# directed graph using adjacency list representation 
class Graph:   
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # add edge to graph 
    def addEdge(self,a,b): 
        self.graph[a].append(b) 
    
    def popnext(self,visited,s):
        visited[s] = True
        print(s, end = ' ')
        print("Visited List = ",visited,"\n")
        for i in self.graph[s]: 
            if visited[i] == False: 
                self.popnext(visited,i)


    # Function to print a DFS of graph 
    def BFS(self, s): 
  
        # Marking all vertices as not visited 
        visited = [False] * (len(self.graph)) 
        # visited is a list of size of the graph.

        print("Visited List = ",visited,"\n")
                    
        self.popnext(visited,s)

        # while queue: 
            
        #     # Dequeue a vertex from  
        #     # queue and print it 
        #     s = queue.pop(0) 
        #     print ("Popped node  = ",s) 
            
        #     print("Now we visit : ",self.graph[s])

        #     # Get all adjacent vertices of the 
        #     # dequeued vertex s. If a adjacent 
        #     # has not been visited, then mark it 
        #     # visited and enqueue it 
        #     for i in self.graph[s]:
        #         if visited[i] == False: 
        #             queue.append(i) 
        #             visited[i] = True

        #     print("Visited List = ",visited,"\n")
  
# Driver code 
  
# Creating a graph
g = Graph() 
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,5) 


print("Adjacency Matrix of the given directed graph is:")
for i in range(0,len(g.graph)+1):
    print(i," -- ",g.graph[i])

print ("Following is Breadth First Traversal"
                  " (starting from vertex 0") 
g.BFS(0)