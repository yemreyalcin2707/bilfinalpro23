import pygame, sys
# pygame kütüphanesinin çağırılması

class Player(pygame.sprite.Sprite):
	#görüntü yönetimi için bütün görsellerin clasa toplanması cod içinde duruma göre klastan çağırılıyor geekforgreeks ve freecodecampten yararlanıldı
	def __init__(self, pos_x, pos_y):
		# kordinat hesabı
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
		#yay hareketi için gerekli olan sıralı fotoğraflama sistemini harekete geçirmek için gerekolan süre ayarı

		if self.yay_hareketi == True:
			self.yay_durum += speed
			self.image = self.yay[int(self.yay_durum)]
			if int(self.yay_durum) == (round(X/10)):
					self.yay_hareketi = False
					
					
					
					
class Button():
	def _init_(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions fareyle üzerine gelme ve tıklanma koşullarına baktık
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action 
					
pygame.init()
clock = pygame.time.Clock()

# oyun ekranı
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")


# yay gruplarını oluşturma
moving_yay = pygame.sprite.Group()
player = Player(50,0)
moving_yay.add(player)


# butonlara görsellerin atanması
cetvel = pygame.image.load("cetvel.png")
buton = pygame.image.load("8kg.png")
buton1 = pygame.image.load("6kg.png")
buton2 = pygame.image.load("4kg.png")
buton3 = pygame.image.load("demir.png")
buton4 = pygame.image.load("Celik.png")
buton5 = pygame.image.load("bakır.png")
buton6 = pygame.image.load("basla.png")
Grafik = pygame.image.load("Yaygrafik.png")

width = cetvel.get_width()
height = cetvel.get_height()
scale = 0.7
cetvel = pygame.transform.scale(cetvel, (int(width * scale), int(height * scale)))
tip1 = Button(350,300,buton5,0.8)
tip2 = Button(350,400,buton3,0.8)
tip3 = Button(350,500,buton4,0.8)
kilo1 = Button(500,300,buton,0.8)
kilo2 = Button(500,400,buton1,0.8)
kilo3 = Button(500,500,buton2,0.8)
Basla = Button(400,600,buton6,1)
State = "seçenek"
font = pygame.font.SysFont("Arial", 25)
Color = ((0,0,0))
Demir = 2
Bakır = 1.5
Celik = 2.5
İsim = "Demir
Tip = 2		
kilo = 4
speed = 0.15			
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
def yay_hesap(K,m):
	global X
	F = m * (9.81)
	X = F/K
	print(round(X/10))

	
	

run = True
while run:
	screen.fill((255, 255, 255))
#ekran rengi belirlenir
	
	#yayın cinsini seçmemiz isteniyor
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
		if kilo1.draw(screen):#yaya uygulanacak kuvveti seçmemiz isteniyor
			kilo = 8
		if kilo2.draw(screen):
			kilo = 6
		if kilo3.draw(screen):
			kilo = 4
		if Basla.draw(screen):#üstte ki atanan komutlar seçildikten sonrasında onlara göre programı devam ettir.
			State= "devam"
	if State == "devam":
		screen.blit(cetvel,(500,40))
		#cetvel ekrana yansıtılır
		screen.blit(Grafik,(565,40))
		moving_yay.draw(screen)
		#yay ekrana yansıtılır
		moving_yay.update(speed)
	if State != any:
		draw_text("Kilo: {} KG ".format(kilo), font,Color,40,250)#ekrana kg bilgileri yansıtılır
		draw_text("Tip: {} ".format(İsim), font,Color,40,300)#ekrana tip bilgileri yazdırılır

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:#ekrana kapatması için gerekli kodlar yazdırılır.
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.calıs()
			print(kilo)
			print(Tip)
			yay_hesap(Tip,kilo)

			
 
		
	pygame.display.flip()
	clock.tick(60)
