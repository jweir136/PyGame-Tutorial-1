# import the module and init pygame
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True

"""
The Camera variables are used to keep track of where the user currently
is in space.
"""
global camera_x; camera_x = 0
global camera_y; camera_y = 0
global camera_z; camera_z = 0
global camera_vertical_angle; camera_vertical_angle = 90
global camera_horizontal_angle; camera_horizontal_angle = 90

if __name__ == "__main__":
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill((255, 255, 255))
		
		"""	DO DRAWING AND RENDERING HERE	"""

		pygame.display.flip()

	
	pygame.quit()
