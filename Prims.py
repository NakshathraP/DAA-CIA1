high=999
v=6
g=[[0,10,0,0,0,8],[0,0,0,2,0,0],[0,1,0,0,0,0],[0,0,-2,0,0,0],
   [0,-4,0,-1,0,0],[0,0,0,0,1,0]]

visited = [0 for i in range(v)]

edge=0

visited[edge]=1

while (edge < v-1):
    minimum = high
    for i in range(v):
        if visited[i]==1:
            for j in range(v):
                if ((visited[j]==0) and g[i][j]):  
                    #print("Inside the loop "+str(i)+"  "+str(j))
                    if minimum > g[i][j]:
                        minimum = g[i][j]
                        x = i
                        y = j
    print(str(x) + "  to  " + str(y) + "  :  " + str(g[x][y]))
    visited[y] = 1
    edge += 1
























































