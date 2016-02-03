import pygame





class jet :
	obj = pygame.image.load("images/obj.png")
	rect = obj.get_rect()
	x_change = 0
	h = 0
	w = 0
	def init(self,x,y):
		self.h = y 
		self.w = x
		self.rect = self.rect.move((self.w/2,self.h - 100))

	def move(self,screen):
		#if self.rect.right <= self.w and self.rect.left >= 0 :
		self.rect = self.rect.move((self.x_change,0))
		screen.blit(self.obj,self.rect)

