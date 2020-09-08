import pygame

from data.scripts.font import Font

class TextButton:
	def __init__(self, text, center, scale=1):
		self.font = Font('data/visuals/font.png')
		self.text = text
		size = self.font.size(self.text, scale)
		self.surfaces = {'active':pygame.Surface(size),
						'inactive':pygame.Surface(size)}
		for surface in self.surfaces:
			self.font.render(self.surfaces[surface], self.text, (0,0), scale)
			self.surfaces[surface].set_colorkey((0, 0, 0))
			self.font.recolor((100, 100, 100))
		self.rect = pygame.Rect((0, 0), size)
		self.rect.center = center

	def draw(self, dest, mousepos):
		if self.rect.collidepoint(mousepos):
			dest.blit(self.surfaces['active'], self.rect)
		else:
			dest.blit(self.surfaces['inactive'], self.rect)