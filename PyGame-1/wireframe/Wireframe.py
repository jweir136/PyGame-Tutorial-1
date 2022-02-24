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
import math
import numpy as np

class Wireframe(object):
	def __init__(self, filename):
		# (1) Look at a list of all the possible nodes
		with open(filename, "r") as f:
			data = json.loads(f.read())
	
		nodes = data["nodes"]
		# (2) Add all the edges to the adj list.
		self._adj_list = {}

		for edge in data["edges"]:
			start = nodes.index(edge["start"])
			end = nodes.index(edge["end"])
			
			if not str(start) in self._adj_list:
				self._adj_list[str(start)] = [end]
			else:
				self._adj_list[str(start)].append(end)
			if not str(end) in self._adj_list:
				self._adj_list[str(end)] = [start]
			else:
				self._adj_list[str(end)].append(start)
		self.nodes = np.zeros((len(nodes), 4))
		for i in range(len(nodes)):
			self.nodes[i,0] = nodes[i]["x"]
			self.nodes[i,1] = nodes[i]["y"]
			self.nodes[i,2] = nodes[i]["z"]
			self.nodes[i,3] = 1

		del nodes

	def addNode(self, x, y, z):
		self.nodes = np.vstack([self.nodes, [x,y,z]])

	def translate(self, axis, d):
		""" Move the entire object (wireframe) over d units) """
		if axis in ['x', 'y', 'z']:
			if axis == 'x':
				dx = d
				dy = 0
				dz = 0
			if axis == 'y':
				dx = 0
				dy = d
				dz = 0
			if axis == 'z':
				dx = 0
				dy = 0
				dz = d
			matrix = np.array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, dx, dy, dz, 1]).reshape(4,4)
			self.nodes = np.dot(self.nodes, matrix)
		else:
			raise Exception("Invalid Axis")

	def scale(self, centre_x, centre_y, scale):
		for node in self.nodes:
			node['x'] = centre_x + scale * (node['x'] - centre_x)
			node['y'] = centre_y + scale * (node['y'] - centre_y)
			node['z'] *= scale
	
	def findCenter(self):
		""" Find center of object """
		num_nodes = len(self.nodes)
		meanX = sum([node['x'] for node in self.nodes]) / num_nodes
		meanY = sum([node['y'] for node in self.nodes]) / num_nodes
		meanZ = sum([node['z'] for node in self.nodes]) / num_nodes
		return (meanX, meanY, meanZ)

	def rotateZ(self, radians):
		c = np.cos(radians)
		s = np.sin(radians)
		matrix = np.array([c, -s, 0, 0, s, c, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]).reshape(4, 4)
		self.nodes = np.dot(self.nodes, matrix)

	def rotateX(self, radians):
		c = np.cos(radians)
		s = np.sin(radians)
		matrix = np.array([1, 0, 0, 0, 0, c, -s, 0, 0, s, c, 0, 0, 0, 0, 1]).reshape(4, 4)
		self.nodes = np.dot(self.nodes, matrix)

	def rotateY(self, radians):
		c = np.cos(radians)
		s = np.sin(radians)
		matrix = np.array([c, 0, s, 0, 0, 1, 0, 0, -s, 0, c, 0, 0, 0, 0, 1]).reshape(4, 4)
		self.nodes = np.dot(self.nodes, matrix)

if __name__ == "__main__":
	w = Wireframe(sys.argv[1])
	print(w.nodes)
	print(w._adj_list)
