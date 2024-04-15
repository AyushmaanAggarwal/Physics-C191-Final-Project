import random
from dimod.sampleset import SampleSet
from dwave.system.composites.embedding import EmbeddedStructure
import networkx as nx
import sys
from collections import defaultdict
from dwave.system import DWaveSampler, EmbeddingComposite

random.seed(10)
n = int(sys.argv[1])
#n=2
G = nx.grid_graph(dim=(n,n,n))
# G_edges = []
# nodes = []
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             nodes.append((i,j,k))
# enumerate(nodes
# for index, node in enumerate(nodes):
#     for index_2, node_2 in enumerate(nodes):
#         if index < index_2:
#             if sum([node[i] - node_2[i] for i in range(3)])==1:
#                 G_edges.append((index, index_2))
# print(G_edges)
# print(nodes)
# exit()
h = {}
J = defaultdict(int)

# Objective
for i, j in G.edges:
    random_val = 2*random.randint(0, 1) - 1
    J[(i, j)] = random_val
    #Q[(j, i)] = random_val

print(J)
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_ising(h, J, num_reads=10)

print(sampleset)
sampleset.to_pandas_dataframe().to_csv("output")
