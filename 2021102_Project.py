# To generate an undirected graph using Snap
import snap

#Create an undirected graph
graph1 = snap.TUNGraph.New()
graph1.AddNode(0)
graph1.AddNode(1)
graph1.AddNode(2)
graph1.AddNode(3)
graph1.AddNode(4)
graph1.AddEdge(0,1)
graph1.AddEdge(1,2)
graph1.AddEdge(2,4)
graph1.AddEdge(4,3)
graph1.AddEdge(3,0)
graph1.AddEdge(1,3)
graph1.AddEdge(1,4)
graph1.SaveEdgeList("generated_graph.txt","Save as tab-separated list of edges")

#To create a petersen graph using Snap
graph2 = snap.TUNGraph.New()
graph2.AddNode(0)
graph2.AddNode(1)
graph2.AddNode(2)
graph2.AddNode(3)
graph2.AddNode(4)
graph2.AddNode(5)
graph2.AddNode(6)
graph2.AddNode(7)
graph2.AddNode(8)
graph2.AddNode(9)
graph2.AddEdge(0,1)
graph2.AddEdge(1,2)
graph2.AddEdge(2,3)
graph2.AddEdge(3,4)
graph2.AddEdge(4,0)
graph2.AddEdge(5,7)
graph2.AddEdge(7,9)
graph2.AddEdge(9,6)
graph2.AddEdge(6,8)
graph2.AddEdge(8,5)
graph2.AddEdge(0,5)
graph2.AddEdge(1,6)
graph2.AddEdge(2,7)
graph2.AddEdge(3,8)
graph2.AddEdge(4,9)
graph2.SaveEdgeList("petersen.txt","Save as tab-separated list of edges")

# DFS Function to traverse the graph
def DFS(lst,snode):
    if visited[snode]!=1:
        dfs_arr.append(snode)
        visited[snode]=1
        for i in lst[snode]:
            if visited[i]!=1:
                DFS(lst,i)

# To check if the graph is connected or not
def check_connected(lst, no_nodes):
    if len(lst)==no_nodes:
        print("The graph is connected")
        return True
    else:
        print("The graph is not connected")
        return False



# To check if the graph is cyclic or not

def check_cycle(lst,snode,parent=-1):
    cycle_visit[snode]=1
    for i in lst[snode]:
        if cycle_visit[i]==0:
            if check_cycle(lst,i,snode):
                return True
        elif i!=parent:
            return True
    return False




# To check if the graph has a hamiltonian cycle or not
ret_flag=False
def check_hamiltonian(lst, snode ,no_nodes):
    count=0
    for i in range(len(hpath)):
        i=i+1
    if i==no_nodes:
        if hpath[-1] in lst[hpath[0]]:
            return True
        else:
            return False
    else:
        for j in lst[snode]:
            if h_visit[j]==0:
                h_visit[j]=1
                hpath.append(j)
                if check_hamiltonian(lst,j,no_nodes):
                    return True
                h_visit[j]=0
                hpath.pop()
                return False

    
# Create a list of all the lines, with each line as String in the list
with open("generated_graph.txt", "r") as f:
    lst = f.readlines()

# Create a twod list with each line as an element in the list and the word being a string in list of lists
twod=[]
for i in range(len(lst)):
    temp=lst[i].split()
    twod.append(temp)

# To get the number of nodes in the graph
for i in range(len(twod)):
    if twod[i][1] == "Nodes:":
        nodes = int(twod[i][2])

# To store the edges in a list
edges=[]
for i in range(len(twod)):
    if twod[i][1]=="NodeId":
        for j in range(i+1,len(twod)):
            edges.append(twod[j])


# To create an adjacency matrix for the graph
adj_lst={}

for i in range(len(edges)):
    if int(edges[i][0]) not in adj_lst:
        adj_lst[int(edges[i][0])]=[]
        adj_lst[int(edges[i][1])]=[]
        adj_lst[int(edges[i][0])].append(int(edges[i][1]))
        adj_lst[int(edges[i][1])].append(int(edges[i][0]))
    else:
        adj_lst[int(edges[i][0])].append(int(edges[i][1]))
        if int(edges[i][1]) not in adj_lst:
            adj_lst[int(edges[i][1])]=[]
            adj_lst[int(edges[i][1])].append(int(edges[i][0]))
        else:
            adj_lst[int(edges[i][1])].append(int(edges[i][0]))
print("The adj_lst for the generate graph is:\n",adj_lst)


connect_flag=False
cycle_flag=False
hamiltonian_flag=False

# To check if the graph is connected or not
visited=[0]*nodes
dfs_arr=[]
DFS(adj_lst,0)
connect_flag=check_connected(dfs_arr, nodes)

# To check if the graph is cyclic or not
cycle_visit=[0]*nodes
cycle_flag=check_cycle(adj_lst,0)
if cycle_flag == True:
    print("The graph is cyclic")
else:
    print("The graph is acyclic")

# To check if the graph has a hamiiltonian cycle or not
if connect_flag==True and cycle_flag==True:
    hpath=[]

    # Checks the Hamiltonian cycle for each node
    for i in range (nodes):
        hpath=[i]
        h_visit=[0]*nodes
        h_visit[i]=1
        hamiltonian_flag=check_hamiltonian(adj_lst,i,nodes)
        if hamiltonian_flag==True:
            print("The graph has a hamiltonian cycle")
            hpath.append(hpath[0])
            print("The hamiltonian cycle is: ",hpath)
            break
    if hamiltonian_flag==False:
        print("The graph does not have a hamiltonian cycle")

elif connect_flag==False and cycle_flag==False:
    print("The graph does not have a hamiltonian cycle")
        

## To prove whether the petersan graph is hamiltonian or not
with open("petersen.txt", "r") as f:
    lst = f.readlines()
# Create a twod list with each line as an element in the list and the word being a string in list of lists
twod=[]
for i in range(len(lst)):
    temp=lst[i].split()
    twod.append(temp)

# To get the number of nodes in the graph
for i in range(len(twod)):
    if twod[i][1] == "Nodes:":
        nodes = int(twod[i][2])

# To store the edges in a list
edges=[]
for i in range(len(twod)):
    if twod[i][1]=="NodeId":
        for j in range(i+1,len(twod)):
            edges.append(twod[j])


# To create an adjacency matrix for the graph
adj_lst={}

for i in range(len(edges)):
    if int(edges[i][0]) not in adj_lst:
        adj_lst[int(edges[i][0])]=[]
        adj_lst[int(edges[i][1])]=[]
        adj_lst[int(edges[i][0])].append(int(edges[i][1]))
        adj_lst[int(edges[i][1])].append(int(edges[i][0]))
    else:
        adj_lst[int(edges[i][0])].append(int(edges[i][1]))
        if int(edges[i][1]) not in adj_lst:
            adj_lst[int(edges[i][1])]=[]
            adj_lst[int(edges[i][1])].append(int(edges[i][0]))
        else:
            adj_lst[int(edges[i][1])].append(int(edges[i][0]))
print()
print("The adj_lst for the petersen graph is:\n",adj_lst)
hamiltonian_flag=False
hpath=[]

# Checks the Hamiltonian cycle for each node
for i in range (nodes):
    hpath=[i]
    h_visit=[0]*nodes
    h_visit[i]=1
    hamiltonian_flag=check_hamiltonian(adj_lst,i,nodes)
    if hamiltonian_flag==True:
        print("The petersen graph has a hamiltonian cycle")
        hpath.append(hpath[0])
        print("The hamiltonian cycle is: ",hpath)
        break
if hamiltonian_flag==False:
    print("The petersen graph does not have a hamiltonian cycle")













