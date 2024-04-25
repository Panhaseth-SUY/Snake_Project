import pygame,sys,random
from pygame.math import Vector2
from object import *
from style import *
cell_size = 40
cell_number = 20

class Game(SNAKE,FRUIT):
	def __init__(self):
		pygame.mixer.pre_init(44100,-16,2,512)
		pygame.init()
		self.screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
		clock = pygame.time.Clock()
		self.game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
		self.game_font1 = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
		self.apple = pygame.image.load('Graphics/apple.png').convert_alpha()

		SCREEN_UPDATE = pygame.USEREVENT
		pygame.time.set_timer(SCREEN_UPDATE,150)

		self.call_object()
		

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == SCREEN_UPDATE:
					self.update()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP or event.key == pygame.K_w:
						if self.snake.direction.y != 1:
							self.snake.direction = Vector2(0,-1)
					if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
						if self.snake.direction.x != -1:
							self.snake.direction = Vector2(1,0)
					if event.key == pygame.K_DOWN or event.key == pygame.K_s:
						if self.snake.direction.y != -1:
							self.snake.direction = Vector2(0,1)
					if event.key == pygame.K_LEFT or event.key == pygame.K_a:
						if self.snake.direction.x != 1:
							self.snake.direction = Vector2(-1,0)

			self.screen.fill((175,215,70))
			self.draw_elements()
			pygame.display.update()
			clock.tick(60)
	def call_object(self):
		self.snake = SNAKE(cell_number = cell_number, cell_size=cell_size, screen=self.screen)
		self.fruit = FRUIT(cell_number = cell_number, cell_size=cell_size, screen=self.screen)
		self.player = PLAYER()
	def update(self):
		self.snake.move_snake()
		self.check_collision()
		self.check_fail()

	def draw_elements(self):
		self.draw_grass()
		self.fruit.draw_fruit()
		self.snake.draw_snake()
		self.draw_score()

	def check_collision(self):
		# when head of snake is colliding with food, food will randomly position
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomize()
			self.snake.add_block()
			self.snake.play_crunch_sound()

		#to ensure food will not spawn in snake body
		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()

	def check_fail(self):
		#to ensure snake will not go out of the grid
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.game_over()


		#bite itself condition when body and head in the same position
		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over() #reset

		
	def game_over(self):
		self.snake.reset()

	def draw_grass(self):
		grass_color = (167,209,61)
		for row in range(cell_number):
			#draw row in even position
   			#draw row in even position
			if row % 2 == 0: 
				for col in range(cell_number):
					if col % 2 == 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						#draw in game screen
						pygame.draw.rect(self.screen,grass_color,grass_rect)
			#draw row in odd position
   			#draw row in odd position	
			else:
				for col in range(cell_number):
					if col % 2 != 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(self.screen,grass_color,grass_rect)			
	def draw_score(self):
		score_text = str(len(self.snake.body) - 3)
		score_surface = self.game_font1.render(score_text,True,(56,74,12))
		score_x = int(cell_size * cell_number - 60)
		score_y = int(cell_size)
		score_rect = score_surface.get_rect(center = (score_x,score_y))
		apple_rect = self.apple.get_rect(midright = (score_rect.left,score_rect.centery))
		bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

		pygame.draw.rect(self.screen,(167,209,61),bg_rect)
		self.screen.blit(score_surface,score_rect)
		self.screen.blit(self.apple,apple_rect)
		pygame.draw.rect(self.screen,(56,74,12),bg_rect,2)
	

# def main():
# 	game = Game()

# if __name__ == '__main__':
# 	main()