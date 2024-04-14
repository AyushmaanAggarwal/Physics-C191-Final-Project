import random
from dwave.system.composites.embedding import EmbeddedStructure
import networkx as nx
from collections import defaultdict
from dwave.system import DWaveSampler, EmbeddingComposite

G = nx.cubical_graph()

Q = defaultdict(int)

# Objective
for i, j in G.edges:
    random_val = 2*random.randint(0, 1) - 1
    Q[(i, j)] = random_val
    #Q[(j, i)] = random_val

print(Q)
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q, num_reads=10)

print(sampleset)
