from typing import DefaultDict

'''
    def criticalConnections(self, n: int, connections):
        for i in range(0, n):
            path = 0
            lastpos = 0
            for a in range(0, n):
                if connections[a][0] == i or connections[a][1] == i:
                    path += 1
                    lastpos = a
            if path == 1:
                return [connections[lastpos]]

        return [[]]

    '''


'''
DFS(G)
    for each  vertex u in G.V
        u.color = WHITE
        u.pi = NIL

    time = 0
    for each vertex u in G.V
        if u.color == WHITE
            DFS-VISIT(G, u)

DFS-VISIT(G, u)
    time = time + 1
    u.d = time
    u.color = GRAY
    for each v in G.Adj(u)
        if v.color == WHITE
            v.pi= u
            DFS-VISIT(G, v)

    u.color = BLACK
    time = time + 1
    u.f = time

    
'''
class Solution:

    def criticalConnections(self, n: int, connections):
        color = [0] * n #setting the color of the vertex to WHITE
        pi = [None] * n
        discovery = [0] * n
        finish = [0] * n
        low = [0] * n

        graph = DefaultDict(list)
        for e in connections:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        
        time = 0
        result = []
        for u in graph:
            if color[u] == 0:
                #self.criticalConnectionsHelper(u, graph, time, color, pi, discovery, finish, low)
                #result.append(self.criticalConnectionsHelper(u, graph, time, color, pi, discovery, finish, low, []))
                result = self.criticalConnectionsHelper(u, graph, time, color, pi, discovery, finish, low, [])

        return result



    def criticalConnectionsHelper(self, u, graph, time, color, pi, discovery, finish, low, result):
        time = time + 1
        discovery[u] = time
        low[u] = time
        color[u] = 1 #setting color to Grey
        
        for v in graph[u]:
            if color[v] == 0: #check if the color is white
                pi[v] = u
                self.criticalConnectionsHelper(v, graph, time, color, pi, discovery, finish, low, result)

                low[u] = min(low[u], low[v])
                if low[v] > discovery[u]:
                    print("[%d, %d]" %(u,v))
                    result.append([u, v])
        
            elif v != pi[u]:
                low[u] = min(low[u], discovery[v])
            

        
        color[u] = 2 #setting color to BLACK
        time = time + 1
        finish[u] = time
        
        return result



    def main(self):
        connections = [[0,1],[1,2],[2,0],[1,3]]

        n = 4 # number of servers

        #self.criticalConnections(n, connections)
        result = self.criticalConnections(n, connections)
        print(result)

        connections = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]
        n = 6
        #self.criticalConnections(n, connections)
        #result = self.criticalConnections(n, connections)
        #print(result)

        connections = [[0,1],[0, 3],[0, 2],[1,5],[2, 3],[2, 4],[3, 4]]
        n = 6
        #self.criticalConnections(n, connections)
        result = self.criticalConnections(n, connections)
        print(result)


if __name__=="__main__":
    ourSol = Solution()
    ourSol.main()

'''
    3
  9    2
1  4  5
'''