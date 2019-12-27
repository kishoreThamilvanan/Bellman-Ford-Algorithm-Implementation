import sys

# CSE 310 Assignment submitted by 
#				Naim Youssif 		(ID# 111256860)
#           and Kishore Thamilvanan (ID# 111373510)
#
#
#
#
class Path:
	def __init__(self):
		self.pathTo = ""

class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
        if key == "x":
        	vertex.path.pathTo = vertex.path.pathTo + "x"
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())

class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
        self.path = Path()
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
def bellman_ford(g, source):
    """Return distance where distance[v] is min distance from source to v.
 
    This will return a dictionary distance.
 
    g is a Graph object which can have negative edge weights.
    source is a Vertex object in g.
    """
    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0
 
    
    # x > c > b > e > y 
    for _ in range(len(g) - 1):
        x=1
        for v in g:
            # print(x)
            # x = x+1
            for n in v.get_neighbours():
                val = distance[n]
                distance[n] = min(distance[n], distance[v] + v.get_weight(n))
                if val != distance[n]:
                	n.path.pathTo = v.path.pathTo + "->" + n.key 
                
    return distance

# ******************************************
def parseLine(line):
    parsed = line.split(",")
    return parsed

def findSetVertices(graph):
    index = 0
    directory = []
    for x in graph:
        directory.append(graph[index][0])
        directory.append(graph[index][1])
        index = index+1
    return set(directory)

def findNumberIteration(directory):
    i = -1
    for x in directory:
        i = i+1
    return i

def sortlist(l):
    list2 = []
    for x in l:
        if  x != 'x' and x != 'y':
            list2.append(x)
    list3 = []
    list3.append('x')
    for y in list2:
        list3.append(y)
    list3.append('y')
    return list3
#sys.argv[1]
string = input("what's the name of the graph file? \n> ")
file = open(string,"r")

raw_graph = []

for line in file: 
    line2 = line.strip('\n')
    raw_graph.append(parseLine(line2))

directory = findSetVertices(raw_graph)
num_iter = findNumberIteration(directory)

l = (list(directory))
l = sortlist(l)

g = Graph()

for vertex in l:
    g.add_vertex(vertex)

for edge in raw_graph:
    src = edge[0]
    dest = edge[1]
    weight = int(edge[2])
    g.add_edge(src, dest, weight)


key = 'x'
source = g.get_vertex(key)
distance = bellman_ford(g, source)
print('Min distance from {} to y : '.format(key))
for v in distance:
    if v.get_key() == "y":
        # print('Distance to {}: {}'.format(v.get_key(), distance[v]))
        print(distance[v])
print("Path :")
print(g.get_vertex("y").path.pathTo)


