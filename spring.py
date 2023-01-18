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
