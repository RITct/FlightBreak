import pygame





class jet :
	obj = pygame.image.load("images/spaceship.png")
	obj = pygame.transform.scale(obj,(50,50))
	rect = obj.get_rect()
	x_change = 0
	h = 0
	w = 0
	def init(self,x,y):
		self.h = y 
		self.w = x
		self.rect = self.rect.move((self.w/2,self.h - 60))

	def move(self,screen):
		#if self.rect.right <= self.w and self.rect.left >= 0 :
		if (self.x_change > 0 and self.rect.right <= self.w) or (self.x_change < 0 and self.rect.left >=0):
			self.rect = self.rect.move((self.x_change,0))
		screen.blit(self.obj,self.rect)

