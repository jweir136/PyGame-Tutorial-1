import Wireframe
import pygame
import json

class ProjectionViewer:
	# This takes the size of the window
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((width,height))
		self.background = (10,10,50)

		self.wireframes = {}
		self.displayNodes = True
		self.displayEdges = True
		self.nodeColor = (255,255,255)
		self.edgeColor = (200,200,200)
		self.nodeRadius = 4

	def addWireframe(self, name, filename):
		wireframe = Wireframe.Wireframe(filename)
		self.wireframes[name] = wireframe

	def display(self):
		self.screen.fill(self.background)

		for wireframe in self.wireframes.values():
			if self.displayNodes:
				for node in wireframe.nodes:
					pygame.draw.circle(self.screen, self.nodeColor, (int(node['x']), int(node['y'])), self.nodeRadius, 0)	
			if self.displayEdges:
				for key in wireframe._adj_list.keys():
					start = json.loads(json.dumps(eval(key)))
					for end in wireframe._adj_list[key]:
						pygame.draw.aaline(self.screen, self.edgeColor, (start["x"], start["y"]), (end["x"], end["y"]), 1)

	def run(self):
		running = True

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			self.screen.fill(self.background)
			self.display()
			pygame.display.flip()

if __name__ == "__main__":
	pv = ProjectionViewer(400,300)
	pv.addWireframe("cube-1", "examples/big_cube.json")
	pv.run()
