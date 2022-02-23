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

class Wireframe(object):
	def __init__(self, filename):
		# (1) Look at a list of all the possible nodes
		with open(filename, "r") as f:
			data = json.loads(f.read())
	
		self.nodes = data["nodes"]
		# (2) Add all the edges to the adj list.
		self._adj_list = {}

		for edge in data["edges"]:
			start = self.nodes.index(edge["start"])
			end = self.nodes.index(edge["end"])
			
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

	def translate(self, axis, d):
		""" Move the entire object (wireframe) over d units) """
		if axis in ['x', 'y', 'z']:
			for node in self.nodes:
				node[axis] += d
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

	def rotateZ(self, cx, cy, cz, radians):
		for node in self.nodes:
			x = node['x'] - cx
			y = node['y'] - cy
			d = math.hypot(y, x)
			theta = math.atan2(y, x) + radians
			node['x'] = cx + d * math.cos(theta)
			node['y'] = cy + d * math.sin(theta)

	def rotateX(self, cx, cy, cz, radians):
		for node in self.nodes:
			y = node['y'] - cx
			z = node['z'] - cz
			d = math.hypot(y, z)
			theta = math.atan2(y, z) + radians
			node['z'] = cz + d * math.cos(theta)
			node['y'] = cy + d * math.sin(theta)

	def rotateY(self, cx, cy, cz, radians):
		for node in self.nodes:
			x = node['x'] - cx
			z = node['z'] - cz
			d = math.hypot(x, z)
			theta = math.atan2(x, z) + radians
			node['z'] = cz + d * math.cos(theta)
			node['x'] = cx + d * math.sin(theta)

if __name__ == "__main__":
	w = Wireframe(sys.argv[1])
	w.translate("x", -100)
	print(w.nodes)
	print(w._adj_list)
