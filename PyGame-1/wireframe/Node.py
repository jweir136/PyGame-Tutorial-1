"""
A Node object, containing location data for a single point.
Nodes are used to create objects (aka wireframes).
"""
class Node(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def __str__(self):
		return "Node({}, {}, {})".format(self.x, self.y, self.z)

	def __repr__(self):
		return "Node({}, {}, {})".format(self.x, self.y, self.z)
