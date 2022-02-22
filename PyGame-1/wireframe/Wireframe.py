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

		print(data)	
		# (2) Add all the edges to the adj list.
		pass

if __name__ == "__main__":
	w = Wireframe(sys.argv[1])
