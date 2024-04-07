"""
Struggling Shoppers

Puzzle game made in Tkinter about purchasing tech products

Jeffrey Zang - ICS3UI final game project

Jan 16 - Jan 30, 2023
"""
import tkinter
import random
from PIL import Image,ImageTk

window = tkinter.Tk()

canvas = tkinter.Canvas(window, width=600, height=650)
# create the canvas

def setInitialValues():
	"""ran at beginning of game, sets inital variable values"""
	global size, square, vertical, horizontal, boxes, walls, winx, winy, createdBoxes, createdWalls, score, boxColour, menuItems, font, level1, level2, level3, selectedLevel, moves
	size = 600
	score = 0
	square = 40
	vertical = []
	horizontal = []
	boxes = []
	createdBoxes = []
	walls = []
	createdWalls = []
	winx = size
	menuItems = []
	winy = size
	boxColour = "#d1b9b9"
	font = ('Inter', 20)
	selectedLevel = None
	moves = 0

	level1 = [[ # coordinates for boxes and walls of level 1
		[3, 3], 
		[3, 11], 
		[11, 11], 
		[11, 3], 
	], 
	[
		[2, 2],
		[3, 2],
		[4, 2],

		[7, 5],
		[7, 6],
		[7, 7],

		[10, 10],
		[10, 11],
		[10, 12],

		[0, 13],
		[1, 13],
		[2, 13],
		[3, 13],

		[14, 0],
		[14, 1],
		[14, 2],
		[14, 3],
		[14, 4],
		[14, 5],
		[14, 6],
		[14, 7]
	]]
	level2 = [[ # coordinates for boxes and walls of level 2
		[11, 1],
		[4, 5],
		[12, 4],
		[13, 4],
		[2, 13],
		[5, 13],
		[13, 11]
	],
	[
		[0, 2],
		[1, 2],
		[2, 2],
		[3, 2],
		[4, 2],

		[9, 2],
		[10, 2],
		[11, 2],
		[12, 2],
		[13, 2],
		[14, 2],

		[0,6],
		[1,6],
		[2,6],
		[3,6],
		[4,6],
		[5,6],

		[9,6],
		[10,6],
		[11,6],
		[12,6],
		[13,6],
		[14,6],

		[0,9],
		[1,9],
		[2,9],
		[3,9],

		[1,13],
		[3,14],
		[3,13],
		[3,12],
		[3,11],
		
		[6,14],
		[6,13],
		[7,13],
		[7,12],
		[7,11],
		[7,10],
		[7,9],

		[10,10],
		[11,10],
		[12,10],
		[13,10],

		[13,12],
	]]
	level3 = [[ # coordinates for boxes and walls of level 3
		[3, 3],
		[8, 1],
		[11, 3],
		[3, 6],
		[12, 7],
		[6, 10],
		[8, 10],
		[5, 13],
		[11, 13]
	],
	[
		 [5, 1],
		 [6, 1],
		 [7, 1],
		 [9, 1],
		 [4, 2],
		 [10, 2],
		 [2, 4],
		 [3, 4],
		 [8, 4],
		 [9, 4],
		 [10, 4],
		 [11, 4],
		 [12, 4],
		 [1, 5],
		 [3, 5],
		 [7, 5],
		 [12, 5],
		 [1, 6],
		 [8, 6],
		 [9, 6],
		 [10, 6],
		 [11, 6],
		 [12, 6],
		 [1, 7],
		 [3, 7],
		 [1, 8],
		 [11, 8],
		 [1, 9],
		 [3, 9],
		 [11, 9],
		 [1, 10],
		 [3, 10],
		 [5, 10],
		 [7, 10],
		 [9, 10],
		 [11, 10],
		 [1, 11],
		 [2, 11],
		 [3, 11],
		 [5, 11],
		 [9, 11],
		 [11, 11],
		 [3, 12],
		 [5, 12],
		 [9, 12],
		 [11, 12],
		 [3, 13],
		 [9, 13],
		 [3, 14],
		 [4, 14],
		 [5, 14],
		 [9, 14],
		 [10, 14],
		 [11, 14]
	]]
def incrementMoves():
	"""adds 1 to the move counter and updates the text"""
	global moves, movesText
	moves += 1
	canvas.delete(movesText)
	movesText = canvas.create_text(150, 650-square/2, text=f'Moves: {moves}', font=font)
	canvas.update()
def createLines():
	"""creates gridlines"""
	for i in range(int(size/square)):
		vertical.append(canvas.create_line(i*square, 0, i*square, size))
	for i in range(int(size/square)):
		horizontal.append(canvas.create_line(0, i*square, size, i*square))
	canvas.create_line(0, size, size, size)

def moveUp():
	"""moves character up, checks for collision"""
	global me, shoppingcart, moves
	coords = canvas.coords(me)

	for i in range(len(boxes)): # checks to see if a box needs to move
		box = canvas.coords(boxes[i][0])
		
		if coords[0] == box[0] and box[1] + square == coords[1]:
			if box[1] == 0: return
				
			for j in range(len(boxes)):
				if i == j: continue
				otherbox = canvas.coords(boxes[j][0])
				if box[0] == otherbox[0] and otherbox[1] + square == box[1]:
					return
			for k in range(len(walls)):
				wall = canvas.coords(walls[k])
				if box[0] == wall[0] and wall[1] + square == box[1]:
					return
			canvas.delete(boxes[i][0])
			newbox = canvas.create_rectangle(box[0], box[1]-square, box[2], box[3]-square, fill=boxColour)
			boxes[i][0] = newbox

			canvas.delete(boxes[i][1][0])
			newimage = canvas.create_image(box[0]+square/2,box[1]-square+square/2,image=boxes[i][1][1], anchor='center')
			boxes[i][1][0] = newimage
			
	if coords[1]-square < 0:
		return

	for i in range(len(walls)): # checks to see if there's a wall in the way
		wall = canvas.coords(walls[i])
		if coords[0] == wall[0] and coords[1]-square == wall[1]:
			return

	canvas.delete(me, shoppingcart)
	me = canvas.create_rectangle(coords[0], coords[1]-square, coords[2], coords[3]-square, fill='#c1d2db')
	shoppingcart = canvas.create_image(coords[0]+square/2,coords[1]-square+square/2,image=shoppingcartImg, anchor='center')
	incrementMoves()
	canvas.update()
	# increments the moves and redraws the character
	
def moveLeft():
	"""moves player left"""
	global me, shoppingcart
	coords = canvas.coords(me)
	
	for i in range(len(boxes)): # checks and moves boxes that are in the way
		box = canvas.coords(boxes[i][0])
		
		if coords[1] == box[1] and box[0] + square == coords[0]:
				if box[0] == 0: return

				for j in range(len(boxes)):
					if i == j: continue
					otherbox = canvas.coords(boxes[j][0])
					if box[1] == otherbox[1] and otherbox[0] + square == box[0]:
						return
				for k in range(len(walls)):
					wall = canvas.coords(walls[k])
					if box[1] == wall[1] and wall[0] + square == box[0]:
						return

				canvas.delete(boxes[i][0])
				newbox = canvas.create_rectangle(box[0]-square, box[1], box[2]-square, box[3], fill=boxColour)
				boxes[i][0] = newbox

				canvas.delete(boxes[i][1][0])
				newimage = canvas.create_image(box[0]-square/2,box[1]+square/2,image=boxes[i][1][1], anchor='center')
				boxes[i][1][0] = newimage
			
	if coords[0]-square <0:
		return

	for i in range(len(walls)): # checks for walls in the way
		wall = canvas.coords(walls[i])
		if coords[1] == wall[1] and coords[0]-square == wall[0]:
			return

	canvas.delete(me, shoppingcart)
	me = canvas.create_rectangle(coords[0]-square, coords[1], coords[2]-square, coords[3], fill='#c1d2db')
	shoppingcart = canvas.create_image(coords[0]-square+square/2,coords[1]+square/2,image=shoppingcartImg, anchor='center')
	incrementMoves()
	canvas.update()
	# increments moves and redraws box
	
def moveDown():
	"""moves player down"""
	global me, shoppingcart
	coords = canvas.coords(me) # gets coordinates of player

	for i in range(len(boxes)): # checks box collision
		box = canvas.coords(boxes[i][0])
		if coords[0] == box[0] and box[1] - square == coords[1]:
			if box[3] == size: return

			for j in range(len(boxes)):
				if i == j: continue
				otherbox = canvas.coords(boxes[j][0])
				if box[0] == otherbox[0] and otherbox[1] - square == box[1]:
					return
			for k in range(len(walls)):
				wall = canvas.coords(walls[k])
				if box[0] == wall[0] and wall[1] - square == box[1]:
					return

			canvas.delete(boxes[i][0])
			newbox = canvas.create_rectangle(box[0], box[1]+square, box[2], box[3]+square, fill=boxColour)
			boxes[i][0] = newbox

			canvas.delete(boxes[i][1][0])
			newimage = canvas.create_image(box[0]+square/2,box[1]+square+square/2,image=boxes[i][1][1], anchor='center')
			boxes[i][1][0] = newimage
			# moves box if it gets pushed

	if coords[3]+square > size:
		return

	for i in range(len(walls)): # checks for wall collision
		wall = canvas.coords(walls[i])
		if coords[0] == wall[0] and coords[1]+square == wall[1]:
			return

	canvas.delete(me, shoppingcart)
	me = canvas.create_rectangle(coords[0], coords[1]+square, coords[2], coords[3]+square, fill='#c1d2db')
	shoppingcart = canvas.create_image(coords[0]+square/2,coords[1]+square+square/2,image=shoppingcartImg, anchor='center')
	incrementMoves()
	canvas.update()
	# increments moves and redraws player
	
def moveRight():
	"""moves player right"""
	global me, shoppingcart
	coords = canvas.coords(me)

	for i in range(len(boxes)): # checks for box collision
		box = canvas.coords(boxes[i][0])
		
		if coords[1] == box[1] and box[0] - square == coords[0]:
				if box[2] == size: return

				for j in range(len(boxes)):
					if i == j: continue
					otherbox = canvas.coords(boxes[j][0])
					if box[1] == otherbox[1] and otherbox[0] - square == box[0]:
						return
				for k in range(len(walls)):
					wall = canvas.coords(walls[k])
					if box[1] == wall[1] and wall[0] - square == box[0]:
						return
						
				canvas.delete(boxes[i][0])
				newbox = canvas.create_rectangle(box[0]+square, box[1], box[2]+square, box[3], fill=boxColour)
				boxes[i][0] = newbox

				canvas.delete(boxes[i][1][0])
				newimage = canvas.create_image(box[0]+square+square/2,box[1]+square/2,image=boxes[i][1][1], anchor='center')
				boxes[i][1][0] = newimage

	if coords[2]+square > size:
		return

	for i in range(len(walls)): # wall collision
		wall = canvas.coords(walls[i])
		if coords[1] == wall[1] and coords[0]+square == wall[0]:
			return

	canvas.delete(me)
	canvas.delete(shoppingcart)
	me = canvas.create_rectangle(coords[0]+square, coords[1], coords[2]+square, coords[3], fill='#c1d2db')
	shoppingcart = canvas.create_image(coords[0]+square+square/2,coords[1]+square/2,image=shoppingcartImg, anchor='center')
	incrementMoves()
	canvas.update()
	# moves shopping cart

def reset():
	"""resets screen on enter"""
	global me, shoppingcart, score, scoreText, dollarImg, movesText, moves
	canvas.delete('all') # delete everything
	createLines()
	me = canvas.create_rectangle(0, 0, square, square, fill='#c1d2db')
	shoppingcart = canvas.create_image(square/2, square/2, image=shoppingcartImg)
	# creates lines, the player, and all the boxes
	boxes.clear()
	walls.clear()
	for box in createdBoxes:
		createdBox = canvas.create_rectangle(box[0][0], box[0][1], box[0][0]+square, box[0][1]+square, fill=boxColour)
		createdImage = canvas.create_image(box[0][0]+square/2, box[0][1]+square/2, image=box[1][1])
		boxes.append([createdBox, [createdImage, box[1][1]]])
	for wall in createdWalls:
		createdWall = canvas.create_rectangle(wall[0], wall[1], wall[0]+square, wall[1]+square, fill='black')
		walls.append(createdWall)
	score = 0
	moves = 0
	canvas.delete(scoreText)
	canvas.delete(movesText)
	# reset score and moves
	scoreText = canvas.create_text(480, 650-square/2, text=f'Items bought: {score}/{len(createdBoxes)}', font=font)
	canvas.create_rectangle(winx-square, winy-square, winx, winy, fill='#089E17')
	dollarImg = ImageTk.PhotoImage(Image.open('./assets/dollar.png'))
	canvas.create_image(winx-square/2,winy-square/2,image=dollarImg, anchor='center')
	movesText = canvas.create_text(150, 650-square/2, text=f'Moves: {moves}', font=font)
	canvas.update()
	# dollar sign 

def createObstacles(min, max): 
	"""randomly generates obstacles"""
	global createdBoxes, createdWalls, me, headphones, monitor, watch
	amount = random.randint(min, max)
	
	headphones = ImageTk.PhotoImage(Image.open('./assets/headphones.png'))
	monitor = ImageTk.PhotoImage(Image.open('./assets/monitor.png'))
	watch = ImageTk.PhotoImage(Image.open('./assets/watch.png'))
	images = [headphones, monitor, watch]
	# load possible images
	
	for i in range(amount):
		thing = size/square
		[startX, startY] = [random.randint(0, int(thing-1)) * square, random.randint(0, int(thing-1)) * square]
		# picks a starting square
		if startX == startY == 0: amount += 1; continue
		if [startX, startY] not in createdWalls:
			createdWalls.append([startX, startY])
			wall = canvas.create_rectangle(startX, startY, startX+square, startY+square, fill='black')
			walls.append(wall)
			# makes the first wall
			
			amount = random.randint(4, 5)
			direction = random.randint(0,1)
			for j in range(1, amount):
				if direction == 0:
					if startX-square*amount == 0:
						break
					for k in createdWalls:
						if startX-square*amount == k[0]:
							break
					
					createdWalls.append([startX-square*j, startY])
					wall = canvas.create_rectangle(startX-square*j, startY, startX-square*(j-1), startY+square, fill='black')
					walls.append(wall)
					# makes the next walls in a line
				if direction == 1:
					if startY-square*amount == 0:
						break
					for k in createdWalls:
						if startY-square*amount == k[1]:
							break
					createdWalls.append([startX, startY-square*j])
					wall = canvas.create_rectangle(startX, startY-square*j, startX+square, startY-square*(j-1), fill='black')
					walls.append(wall)
		
		else: amount += 1; continue

	amount = random.randint(min, max)
	i = 0 # picks amount of boxes to make
	while i < amount:
		thing = size/square
		[x, y] = [random.randint(1, int(thing-2)) * square, random.randint(1, int(thing-2)) * square]

		good = True
		if x == y == 0: good = False
		for j in createdBoxes:
			if j[0] == [x, y]: good = False
		for k in createdWalls:
			if k == [x, y]: good = False
		if not good:
			continue
		# makes sure the box is legal
		
		box = canvas.create_rectangle(x, y, x+square, y+square, fill=boxColour)
		selectedImage = random.choice(images)
		createdImage = canvas.create_image(x+square/2,y+square/2,image=selectedImage, anchor='center')
		boxes.append([box, [createdImage, selectedImage]])
		createdBoxes.append([[x, y], [createdImage, selectedImage]])
		i += 1
		# makes the boxes

	for i in walls:
		coords = canvas.coords(i)
		if coords[0] == coords[1] == 0:
			canvas.delete(i)
			canvas.update()
			createdWalls.pop(walls.index(i))
			walls.remove(i)
	# Cleans up bad walls
		
def createLevel(levelBoxes=[], levelWalls=[]):
	"""given coordinates, creates a level"""
	global headphones, monitor, watch, images, inmenu
	headphones = ImageTk.PhotoImage(Image.open('./assets/headphones.png'))
	monitor = ImageTk.PhotoImage(Image.open('./assets/monitor.png'))
	watch = ImageTk.PhotoImage(Image.open('./assets/watch.png'))
	images = [headphones, monitor, watch]
	# loads images
	canvas.delete('all') # clears everything
	for i in levelBoxes:
		box = canvas.create_rectangle(i[0]*square, i[1]*square, i[0]*square+square, i[1]*square+square, fill=boxColour)
		selectedImage = random.choice(images)
		createdImage = canvas.create_image(i[0]*square+square/2,i[1]*square+square/2,image=selectedImage, anchor='center')
		boxes.append([box, [createdImage, selectedImage]])
		createdBoxes.append([[i[0]*square, i[1]*square], [createdImage, selectedImage]])
	# created all boxes
	for i in levelWalls:
		wall = canvas.create_rectangle(i[0]*square, i[1]*square, i[0]*square+square, i[1]*square+square, fill='black')
		walls.append(wall)
		createdWalls.append([i[0]*square, i[1]*square])
	# created all walls
	canvas.update()
	inmenu=False
	# update state
def keyPressed(event):
	"""detect when a key is pressed"""
	global score, scoreText, totalBoxes, inmenu, chosenLevel
	if not inmenu:
		if score >= totalBoxes:
			# checks for winning
			canvas.create_text(size/2, 100, text='You won!', font=font, justify='center', fill='#34c322')
			canvas.create_text(size/2, 250, text='Press Backspace to return to the menu', font=font, justify='center', fill='#34c322')
		if event.keysym in ['Up', 'w']:
			moveUp()
		elif event.keysym in ['Down', 's']:
			moveDown()
		elif event.keysym in ['Right', 'd']:
			moveRight()
		elif event.keysym in ['Left', 'a']:
			moveLeft()
		# movement
		elif event.keysym == 'BackSpace':
			canvas.delete('all')
			inmenu = True
			createMenu()
		elif event.keysym == 'p':
			canvas.delete('all')
			game()
		elif event.keysym == 'Return':
			reset()
			return
		# resetting
	else: # menu controls
		if event.keysym == 'space':
			inmenu = False
			canvas.delete('all')
			game()
		if event.keysym in ['1', '2', '3']:
			game(event.keysym)
			chosenLevel = event.keysym
	for i in range(len(boxes)):
		box = canvas.coords(boxes[i][0])
		if box[0] + square == winx and box[1] + square == winy:
			canvas.delete(boxes[i][0])
			canvas.delete(boxes[i][1][0])
			boxes.pop(i)
			score += 1
			canvas.delete(scoreText)
			scoreText = canvas.create_text(480, 650-square/2, text=f'Items bought: {score}/{totalBoxes}', font=font)
			canvas.update()
			break

def createMenu():
	"""Creates the starting menu"""
	global shoppingcartMenu, dollarMenu, shoppingcartImg, dollarImg, headphones, menuItems, inmenu
	setInitialValues()
	inmenu = True
	box0 = canvas.create_polygon(
		0, 0,
		0, 80,
		40, 40,
		120, 80,
		200, 20,
		240, 40,
		320, 20, 
		400, 40,
		440, 80,
		520, 20,
		600, 80,
		600, 0,
		fill='#009898'
	)
	title = canvas.create_text(size/2, 100, text='Struggling Shoppers', font=font, justify='center')
	description = canvas.create_text(300, 200, text='It\'s Black Friday!\nBuy the tech products by pushing them into the dollar sign.\nBe careful to not make mistakes! \n\nControls:\nPress ENTER to restart.\nUse WASD or arrow keys to move.\nPress P to generate a new level.\nPress backspace to return to this menu.', font=('Inter', 12), justify='center')
	shoppingcartImg = ImageTk.PhotoImage(Image.open('./assets/shoppingcart.png'))
	shoppingcartSquare = canvas.create_rectangle(140, 300, 140+square, 300+square, fill='#c1d2db')
	shoppingcartMenu = canvas.create_image(140+square/2,300+square/2,image=shoppingcartImg, anchor='center')
	arrow1 = canvas.create_line(200, 320, 280, 320, width='3', arrow=tkinter.LAST)

	headphones = ImageTk.PhotoImage(Image.open('./assets/headphones.png'))
	boxMenu = canvas.create_rectangle(300, 300, 300+square, 300+square, fill=boxColour)
	createdImage = canvas.create_image(300+square/2,300+square/2,image=headphones, anchor='center')
	arrow2 = canvas.create_line(360, 320, 440, 320, width='3', arrow=tkinter.LAST)

	dollarbox = canvas.create_rectangle(460, 300, 460+square, 300+square, fill='#089E17')
	dollarImg = ImageTk.PhotoImage(Image.open('./assets/dollar.png'))
	dollarMenu = canvas.create_image(460+square/2,300+square/2,image=dollarImg, anchor='center')

	among = canvas.create_text(size/2, 450, text='Press 1, 2, or 3 to start a new level', font=font, justify='center')
	among2 = canvas.create_text(size/2, 550, text='Press Space to start a\nrandomly generated level\nNote: a randomly generated level\nmay not be possible to beat', font=font, justify='center')
	menuItems += [box0, title, description, shoppingcartImg, shoppingcartSquare, shoppingcartMenu, arrow1, headphones, boxMenu, createdImage, arrow2, dollarbox, dollarImg, dollarMenu, among, among2]
	
def game(level=None):
	"""Runs game"""
	global me, boxes, walls, img, shoppingcart, score, scoreText, totalBoxes, shoppingcartImg, dollar, dollarImg, movesText
	
	setInitialValues()
	if not level:
		createObstacles(7, 10)
	elif level == '1':
		createLevel(level1[0], level1[1])
	elif level == '2':
		createLevel(level2[0], level2[1])
	elif level =='3':
		createLevel(level3[0], level3[1])
	# loads specific levels
	createLines()
	print(len(createdBoxes))

	me = canvas.create_rectangle(0, 0, square, square, fill='#c1d2db')

	shoppingcartImg = ImageTk.PhotoImage(Image.open('./assets/shoppingcart.png'))
	shoppingcart = canvas.create_image(square/2,square/2,image=shoppingcartImg, anchor='center')
	# creates shopping cart

	canvas.create_rectangle(winx-square, winy-square, winx, winy, fill='#089E17')
	dollarImg = ImageTk.PhotoImage(Image.open('./assets/dollar.png'))
	dollar = canvas.create_image(winx-square/2,winy-square/2,image=dollarImg, anchor='center')
	# creates dollar
	totalBoxes = len(boxes)
	scoreText = canvas.create_text(470, 650-square/2, text=f'Items bought: {score}/{totalBoxes}', font=font)
	movesText = canvas.create_text(150, 650-square/2, text=f'Moves: {moves}', font=font)
	# creates score and move counter

createMenu()
# creates starting menu

canvas.bind("<Key>", keyPressed)

canvas.pack()

canvas.focus_set()
window.mainloop()

# keybinds and stuff