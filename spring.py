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
