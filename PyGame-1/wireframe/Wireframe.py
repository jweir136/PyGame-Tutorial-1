"""
This is a wireframe, used to hold a collection of nodes and edges.
At its core, a Wireframe is just a graph.

We represent the connections using an adjacency list. You are required to 
specify the number of nodes in the wireframe.

An input file is a JSON file. It has the following sections

	{"nodes": [<a list of nodes in format {"x","y","z"}>], "edges":[<a list of edges in the format {"start":{"x","y","z"}, "end":{"x","y","z"}}>]}
"""
import json
import sys

class Wireframe(object):
	def __init__(self, filename):
		# (1) Look at a list of all the possible nodes
		with open(filename, "r") as f:
			data = json.loads(f.read())
	
		self.nodes = data["nodes"]
		# (2) Add all the edges to the adj list.
		self._adj_list = {}

		for edge in data["edges"]:
			start = edge["start"]
			end = edge["end"]
			if not str(start) in self._adj_list:
				self._adj_list[str(start)] = [end]
			else:
				self._adj_list[str(start)].append(end)
			if not str(end) in self._adj_list:
				self._adj_list[str(end)] = [start]
			else:
				self._adj_list[str(end)].append(start)

	def addNode(self, x, y, z):
		newNode = {"x":x,"y":y,"z":z}
		if not str(newNode) in self.nodes:
			self.nodes.append(newNode)

if __name__ == "__main__":
	w = Wireframe(sys.argv[1])
