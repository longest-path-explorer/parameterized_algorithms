from collections import defaultdict

class Graph:
    def __init__(self, n: int | None = None, m: int | None = None, max_degree: int | None = None, min_degree: int | None = 0, max_weight: int | None = None, min_weight: int | None = 0, directed: bool = False, weighted: bool = False, connected: bool = False, allow_self_loops: bool = False, allow_multiple_edges: bool = False, seed: int | None = None, one_indexed: bool = False, type: str | None = None):
        self.edges = defaultdict(list)
        self.n = n
        self.m = m
        self.max_degree = max_degree
        self.min_degree = min_degree
        self.max_weight = max_weight
        self.min_weight = min_weight
        self.directed = directed
        self.weighted = weighted
        self.connected = connected
        self.allow_self_loops = allow_self_loops
        self.allow_multiple_edges = allow_multiple_edges
        self.seed = seed
        self.one_indexed = one_indexed
        self.type = type
    
    def __str__(self) -> str:
        return str(self.edges)
    
    def add_edge(self, u: int, v: int, w: int | None = None) -> None:
        if self.weighted:
            self.edges[u].append((v, w))
            if not self.directed:
                self.edges[v].append((u, w))
        else:
            self.edges[u].append(v)
            if not self.directed:
                self.edges[v].append(u)
    
    @property
    def n(self) -> int:
        return self._n
    
    @n.setter
    def n(self, n: int | None) -> None:
        self._n = n
    
    @property
    def m(self) -> int:
        return self._m
    
    @m.setter
    def m(self, m: int | None) -> None:
        self._m = m
    
    @property
    def max_degree(self) -> int:
        return self._max_degree
    
    @max_degree.setter
    def max_degree(self, max_degree: int | None) -> None:
        self._max_degree = max_degree
    
    @property
    def min_degree(self) -> int:
        return self._min_degree
    
    @min_degree.setter
    def min_degree(self, min_degree: int | None) -> None:
        self._min_degree = min_degree
    
    @property
    def max_weight(self) -> int:
        return self._max_weight
    
    @max_weight.setter
    def max_weight(self, max_weight: int | None) -> None:
        self._max_weight = max_weight
    
    @property
    def min_weight(self) -> int:
        return self._min_weight
    
    @min_weight.setter
    def min_weight(self, min_weight: int | None) -> None:
        self._min_weight = min_weight
    
    @property
    def directed(self) -> bool:
        return self._directed
    
    @directed.setter
    def directed(self, directed: bool) -> None:
        self._directed = directed
    
    @property
    def weighted(self) -> bool:
        return self._weighted
    
    @weighted.setter
    def weighted(self, weighted: bool) -> None:
        self._weighted = weighted
    
    @property
    def connected(self) -> bool:
        return self._connected
    
    @connected.setter
    def connected(self, connected: bool) -> None:
        self._connected = connected
        
    @property
    def allow_self_loops(self) -> bool:
        return self._allow_self_loops
    
    @allow_self_loops.setter
    def allow_self_loops(self, allow_self_loops: bool) -> None:
        self._allow_self_loops = allow_self_loops
    
    @property
    def allow_multiple_edges(self) -> bool:
        return self._allow_multiple_edges
    
    @allow_multiple_edges.setter
    def allow_multiple_edges(self, allow_multiple_edges: bool) -> None:
        self._allow_multiple_edges = allow_multiple_edges
    
    @property
    def seed(self) -> int:
        return self._seed
    
    @seed.setter
    def seed(self, seed: int | None) -> None:
        self._seed = seed
    
    @property
    def one_indexed(self) -> bool:
        return self._one_indexed
    
    @one_indexed.setter
    def one_indexed(self, one_indexed: bool) -> None:
        self._one_indexed = one_indexed
    
    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, type: str | None) -> None:
        self._type = type
    
    @property
    def edges(self) -> defaultdict[list]:
        return self._edges
    
    @edges.setter
    def edges(self, edges: defaultdict[list]) -> None:
        self._edges = edges