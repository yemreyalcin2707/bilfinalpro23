import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		global ters
		super().__init__()
		self.yay_hareketi = False
		self.yay = []
		
		self.yay.append(pygame.image.load('-1.5.png'))
		self.yay.append(pygame.image.load('-1.png'))
		self.yay.append(pygame.image.load('-0.5.png'))
		self.yay.append(pygame.image.load('0.png'))
		self.yay.append(pygame.image.load('0.5.png'))
		self.yay.append(pygame.image.load('1.png'))
		self.yay.append(pygame.image.load('1.5.png'))
		self.yay.append(pygame.image.load('2.png'))
		self.yay_durum = 0
		self.image = self.yay[self.yay_durum]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def calıs(self):
		self.yay_hareketi = True

	def update(self,speed):

		if self.yay_hareketi == True:
			self.yay_durum += speed
			self.image = self.yay[int(self.yay_durum)]
			if int(self.yay_durum) == (round(X/10)):
					self.yay_hareketi = False
			
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
def yay_hesap(K,m):
	global X
	F = m * (9.81)
	X = F/K

run = True
while run:
	screen.fill((255, 255, 255))

	
	
	if State == "seçenek":
		if tip1.draw(screen):
			Tip = Bakır
			İsim = "Bakır"
		if tip2.draw(screen):
			Tip = Demir
			İsim = "Demir"
		if tip3.draw(screen):
			Tip = Celik
			İsim = "Celik"
		if kilo1.draw(screen):
			kilo = 8
		if kilo2.draw(screen):
			kilo = 6
		if kilo3.draw(screen):
			kilo = 4
		if Basla.draw(screen):
			State= "devam"
	if State == "devam":
		screen.blit(cetvel,(500,40))
		moving_yay.draw(screen)
		moving_yay.update(speed)
	if State != any:
		draw_text("Kilo: {} KG ".format(kilo), font,Color,40,250)
		draw_text("Tip: {} ".format(İsim), font,Color,40,300)

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.calıs()
			print(kilo)
			print(Tip)
			yay_hesap(Tip,kilo)

			
 
		
	pygame.display.flip()
	clock.tick(60)
