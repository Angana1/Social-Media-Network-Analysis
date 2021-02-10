import snap

#loading graph in G1
G1 = snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)

n=G1.GetNodes() #stores number of nodes


#CLOSENESS CENTRALITY CALCULATION

NIdToDistH = snap.TIntH()#hash table to store shortest paths to all other nodes.

file_closeness=open("closeness.txt","w+")

mydict={}#dictionary to store node id and closeness centrality value
for node in G1.Nodes():
    sum=0
    shortestPath = snap.GetShortPath(G1, node.GetId(), NIdToDistH)
    for key in NIdToDistH:
        sum=sum+NIdToDistH[key]
    closeness_centrality=(n-1)/sum
    mydict.update({node.GetId():closeness_centrality})

#sorted_dict stores closeness centrality values sorted by centrality.
sorted_dict=sorted(mydict.items(), key=lambda x: x[1], reverse=True)

#the following code prints the values into the text file
for i in sorted_dict:
    #str1=str(i[0])+" "+str("%0.6f"i[1])+"\n"
    str1="%d %0.6f\n"%(i[0],i[1])
    file_closeness.write(str1)

file_closeness.close()




#BIASED PAGERANK CALCULATION

degVals={} #dictionary degVals stores degree of each node in the form {nodeID: degree}
PR_temp={} #temporary dictionary for simultaneous update in pagerank. We initialise to 0.
for node in G1.Nodes():
    degVals.update({node.GetId():node.GetOutDeg()})
    PR_temp.update({node.GetId():0})


s=0 #num stores number of nodes with degree divisible by 4
for node in G1.Nodes():
    if (node.GetId() % 4 == 0):
        s=s+1


PR={} #dictionary PR stores PageRank values in the form {nodeID: pagerank value}
d={} #dictionary d stores biased preference vectors in the form {nodeID: preference value for the node}

for node in G1.Nodes():
    if(node.GetId()%4==0):
        d.update({node.GetId():(1/s)})
        PR.update({node.GetId():(1/s)})
    else:
        d.update({node.GetId():0})
        PR.update({node.GetId():0})


for j in range(0,100):
    for node in G1.Nodes():
        sum1 = 0  # sum stores the sum of (PR/outdegree) values for every neighbour of the current node
        for neighbourID in node.GetOutEdges():
            sum1 = sum1 + (PR[neighbourID] / degVals[neighbourID])
        PR_temp[node.GetId()] = (0.8 * sum1) + (0.2 * d[node.GetId()])
    sum_of_PRs=0
    for key in PR_temp:
        sum_of_PRs=sum_of_PRs+PR_temp[key]
    #values=PR_temp.values()
    #sum_of_PRs = sum(values)
    for node in G1.Nodes():
        PR[node.GetId()] = PR_temp[node.GetId()] / sum_of_PRs



sorted_PR_dict=sorted(PR.items(), key=lambda x: x[1], reverse=True)


#following code prints the pagerank values into a text file
file_pagerank=open("pagerank.txt","w+")
for i in sorted_PR_dict:
    str2="%d %0.6f\n"%(i[0],i[1])
    file_pagerank.write(str2)

file_pagerank.close()











