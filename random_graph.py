import random
from graph import Graph

class RandomGraph(Graph):
    def __init__(self, n: int | None = None, m: int | None = None, max_degree: int | None = None, min_degree: int | None = 0, max_weight: int | None = None, min_weight: int | None = 0, directed: bool = False, weighted: bool = False, connected: bool = False, allow_self_loops: bool = False, allow_multiple_edges: bool = False, seed: int | None = None, one_indexed: bool = False, type: str | None = None, edge_probability: float = 0.5, weight_distribution: str = 'uniform'):
        super().__init__(n, m, max_degree, min_degree, max_weight, min_weight, directed, weighted, connected, allow_self_loops, allow_multiple_edges, seed, one_indexed, type)
        self.n = n
        self.edge_probability = edge_probability