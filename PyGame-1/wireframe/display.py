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
					start = wireframe.nodes[int(key)]
					for idx in wireframe._adj_list[key]:
						end = wireframe.nodes[idx]
						pygame.draw.aaline(self.screen, self.edgeColor, (start['x'], start['y']), (end['x'], end['y']), 1)
					
	def run(self):
		running = True

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						for wireframe in self.wireframes:
							self.wireframes[wireframe].translate("x", -10)
					elif event.key == pygame.K_RIGHT:
						for wireframe in self.wireframes:
							self.wireframes[wireframe].translate("x", 10)
					elif event.key == pygame.K_UP:
						for wireframe in self.wireframes:
							self.wireframes[wireframe].translate("y", -10)
					elif event.key == pygame.K_DOWN:
						for wireframe in self.wireframes:
							self.wireframes[wireframe].translate("y", 10)
					elif event.key == pygame.K_MINUS:
						for wireframe in self.wireframes:
							self.wireframes[wireframe].scale(self.width/2, self.height/2, 0.8)
					elif event.key == pygame.K_EQUALS:
						for wireframe in self.wireframes:
							self.wireframes[wireframe].scale(self.width/2, self.height/2, 1.25)

			self.screen.fill(self.background)
			self.display()
			pygame.display.flip()
			

if __name__ == "__main__":
	pv = ProjectionViewer(400,300)
	pv.addWireframe("cube-1", "examples/big_cube.json")
	pv.run()
