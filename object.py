import pygame,sys,random
from pygame.math import Vector2


class SNAKE:
	def __init__(self, cell_size, cell_number, screen):
		self.cell_size = cell_size
		self.cell_number = cell_number
		self.screen = screen
		#snake head body tail with 3 vectors
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)
		self.new_block = False
		#define graphic for snake head body and tail
		self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
		self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
		self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
		self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
		
		self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
		self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
		self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
		self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

		self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
		self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

		self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
		self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
		self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
		self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

		self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
		self.eat_sound = pygame.mixer.Sound('Sound/ding.mp3')
		
	#draw_snake() hold update_head_graphics() and update_body_graphics()
	def draw_snake(self):
		#choose graphics for head and tail
		self.update_head_graphics()
		self.update_tail_graphics()
		#choose graphic for body
		#and place head body and tail on screen
		for index,block in enumerate(self.body):
			#block is vector(x,y)
			x_pos = int(block.x * self.cell_size)
			y_pos = int(block.y * self.cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,self.cell_size,self.cell_size)
			
			#place head in its vector position
			if index == 0:
				self.screen.blit(self.head,block_rect)
			#place tail in its vector position
			elif index == len(self.body) - 1:
				self.screen.blit(self.tail,block_rect)
			#place body in its vector position
			else:
				#check in front and backward block to define horizontal or vertical body (must true in these two condition)
				previous_block = self.body[index + 1] - block #current block with next block sidetail 
				next_block = self.body[index - 1] - block #current block with next block side head
				if previous_block.x == next_block.x:
					self.screen.blit(self.body_vertical,block_rect)
				elif previous_block.y == next_block.y:
					self.screen.blit(self.body_horizontal,block_rect)
				else:
					#define curve body
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						self.screen.blit(self.body_tl,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						self.screen.blit(self.body_bl,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						self.screen.blit(self.body_tr,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						self.screen.blit(self.body_br,block_rect)

	def update_head_graphics(self):
		# define direction of head
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left
		elif head_relation == Vector2(-1,0): self.head = self.head_right
		elif head_relation == Vector2(0,1): self.head = self.head_up
		elif head_relation == Vector2(0,-1): self.head = self.head_down

	def update_tail_graphics(self):
		# define direction of tail
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	def move_snake(self):
		#check self.new_block in init function if you want to know where is it and it defaults values is False
		# self.direction is also and defaults value is Vector2(0,0)
		# self.new_block will be True if add_block() is called
		if self.new_block == True:
			#assign body element(vectors) to body_copy 
			body_copy = self.body[:]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			#did not include tail 
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]

	def add_block(self):
		self.new_block = True

	def play_crunch_sound(self):
		self.snake_eat_sound = random.choice([self.eat_sound, self.crunch_sound])
		self.snake_eat_sound.play()
	

	def reset(self):
		#set it to init value
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)


class FRUIT:
	def __init__(self,cell_size, cell_number, screen):
		self.cell_size = cell_size
		self.cell_number = cell_number

		self.apple = pygame.image.load("resources/3-removebg-preview.png").convert_alpha()
		self.hamburger = pygame.image.load("resources/1-removebg-preview.png").convert_alpha()
		self.cake = pygame.image.load("resources/2-removebg-preview.png").convert_alpha()
		self.water_melons = pygame.image.load("resources/4-removebg-preview.png").convert_alpha()
		self.screen = screen
		self.randomize()

		
	def draw_fruit(self):
		fruit_rect = pygame.Rect(int(self.pos.x * self.cell_size),int(self.pos.y * self.cell_size),self.cell_size,self.cell_size)
		self.screen.blit(self.food,fruit_rect)
		
		#pygame.draw.rect(screen,(126,166,114),fruit_rect)

	def randomize(self):
		self.food = random.choice([self.apple, self.hamburger, self.cake, self.water_melons])
		#choose random coordinates for food
		self.x = random.randint(0,self.cell_number - 1)
		self.y = random.randint(0,self.cell_number - 1)
		self.pos = Vector2(self.x,self.y)


