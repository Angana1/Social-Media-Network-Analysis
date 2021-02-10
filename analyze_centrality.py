import snap

G1 = snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)

n=G1.GetNodes() #stores number of nodes

#CLOSENESS CENTRALITY -
#hash_closeness is a hash table that stores the node ID and corresponding closeness centrality.
hash_closeness=snap.TIntFltH()
for node in G1.Nodes():
    hash_closeness[node.GetId()] = snap.GetClosenessCentr(G1, node.GetId())

#BETWEENNESS CENTRALITY -
#hash_betweenness is a hash table that stores the node ID and corresponding betweenness centrality.
hash_betweenness = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(G1, hash_betweenness, Edges, 0.8)

#PAGERANK -
##hash_pagerank is a hash table that stores the node ID and corresponding pagerank value.
hash_pagerank = snap.TIntFltH()
snap.GetPageRank(G1, hash_pagerank)




