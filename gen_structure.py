import sys
import snap
Rnd = snap.TRnd(42)
Rnd.Randomize()

#Generating subgraph 1(facebook.elist)
G1 = snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)
V1 = snap.TIntV()

for node in G1.Nodes():
  if ((node.GetId()%5)==0):
      V1.Add(node.GetId())


snap.DelNodes(G1,V1)
snap.SaveEdgeList(G1,"facebook.elist")


#Generating subgraph 2(amazon.elist)
G2 = snap.LoadEdgeList(snap.PUNGraph, "com-amazon.ungraph.txt", 0, 1)
V2 = snap.TIntV()

for node in G2.Nodes():
    if node.GetId()%4!=0:
        V2.Add(node.GetId())

snap.DelNodes(G2,V2)
snap.SaveEdgeList(G2,"amazon.elist")

file_name=sys.argv[1]
Graph1=snap.LoadEdgeList(snap.PUNGraph,file_name, 0, 1)

#1.Size of the network
node_count=Graph1.GetNodes()
print("Number of nodes: ",node_count)
edge_count=Graph1.GetEdges()
print("Number of edges: ",edge_count)

#2.Degree of nodes in the network
node_deg7=snap.CntDegNodes(Graph1,7)
print("Number of nodes with degree=7: ",node_deg7)

max_deg=0#to store the highest degree of the graph
nodes_max=[]#list to store node IDs of nodes with highest degree
for node in Graph1.Nodes():
    if node.GetDeg()>max_deg:
        max_deg=node.GetDeg()
#print("Max degree:",max_deg)
for node in Graph1.Nodes():
    if node.GetDeg()==max_deg:
        nodes_max.append(node.GetId())

nodesmaxstring=','.join(map(str,nodes_max)) #converting list to comma separated string
print("Node id(s) with highest degree: %s"%nodesmaxstring)

str="deg_dist_"+file_name
snap.PlotInDegDistr(Graph1,str,"Degree Distribution")


#3.Paths in the Network
full1 = snap.GetBfsFullDiam(Graph1, 10, False)
full2 = snap.GetBfsFullDiam(Graph1, 100, False)
full3 = snap.GetBfsFullDiam(Graph1, 1000, False)
print("Approximate full diameter by sampling ",10," nodes: ",full1)
print("Approximate full diameter by sampling ",100," nodes: ",full2)
print("Approximate full diameter by sampling ",1000," nodes: ",full3)
fmean=(full1+full2+full3)/3.0
fvar=(((full1*full1)+(full2*full2)+(full3*full3))/3.0)-(fmean*fmean)
print("Approximate full diameter (mean and variance): %0.4f,%0.4f"%(fmean,fvar))

eff1 = snap.GetBfsEffDiam(Graph1, 10, False)
eff2 = snap.GetBfsEffDiam(Graph1, 100, False)
eff3 = snap.GetBfsEffDiam(Graph1, 1000, False)
print("Approximate effective diameter by sampling ",10," nodes: %0.4f"%eff1)
print("Approximate effective diameter by sampling ",100," nodes: %0.4f"%eff2)
print("Approximate effective diameter by sampling ",1000," nodes: %0.4f"%eff3)
effmean=(eff1+eff2+eff3)/3.0
effvar=(((eff1*eff1)+(eff2*eff2)+(eff3*eff3))/3.0)-(effmean*effmean)
print("Approximate effective diameter (mean and variance): %0.4f,%0.4f"%(effmean,effvar))

str1='shortest_path_'+file_name
snap.PlotShortPathDistr(Graph1, str1, "Distribution of shortest path lengths")


#4.Components of the network
fraction=snap.GetMxSccSz(Graph1)
print("Fraction of nodes in largest connected component: %0.4f"%fraction)

V_edges=snap.TIntPrV()
snap.GetEdgeBridges(Graph1,V_edges)
edge_bridges=V_edges.Len()
print("Number of edge bridges: ",edge_bridges)

Art_points=snap.TIntV()
snap.GetArtPoints(Graph1,Art_points)
art=Art_points.Len()
print("Number of articulation points: ",art)

str2="connected_comp_"+file_name
snap.PlotSccDistr(Graph1,str2,"Distribution of sizes of connected components")



#5.Connectivity and clustering in the network
avg_cc=snap.GetClustCf(Graph1,-1)
print("Average clustering coefficient: %0.4f"%avg_cc)
triads=snap.GetTriads(Graph1,-1)
print("Number of triads: ",triads)

random1=Graph1.GetRndNId(Rnd)
node_cc=snap.GetNodeClustCf(Graph1,random1)
print("Clustering coefficient of random node %d: %0.4f"%(random1,node_cc))

random2=Graph1.GetRndNId(Rnd)
node_triads=snap.GetNodeTriads(Graph1,random2)
print("Number of triads random node %d participates: %d"%(random2,node_triads))

triad_edges=snap.GetTriadEdges(Graph1,-1)
print("Number of edges that participate in at least one triad: ",triad_edges)

str3="clustering_coeff_"+file_name
snap.PlotClustCf(Graph1,str3,"The distribution of clustering coefficient")



