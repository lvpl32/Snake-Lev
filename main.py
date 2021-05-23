import pygame
import sys
import random
import time



pygame.init()


class Game():
    def __init__(self):
        self.scr_width = 720
        self.scr_height = 460



        self.red = (255,0,0)
        self.green = (0,255,0)
        self.white = (255,255,255)
        self.black = (0,0,0)


        self.fps = pygame.time.Clock()
        self.score = 0

    def surface(self):
        self.play_surface = pygame.display.set_mode((self.scr_width,self.scr_height))
        pygame.display.set_caption('Snake')

    def event_loop(self,change_to):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('w'):
                        change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                        change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                        change_to = "UP"
                elif event.key == pygame.K_DOWNT or event.key == ord('s'):
                        change_to = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to

    def refresh_screen(self):
        pygame.display.flip()
        Game.fps.tick(23)
    def game_over(self):
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surf, go_rect)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

class Snake():
    def __init__(self, snake_color):
        self.snake_head_position = [100,50]

        self.snake_body = [[100,50],[90,50],[80,50]]
        self.snake_color = snake_color
        self.movemenet_direction = "RIGHT"
        self.change_to = self.movemenet_direction

    def change_directions(self):
        if any((self.change.to == "RIGHT" and not self.movemenet_direction == "LEFT", self.change_to == "LEFT" and not self.movemenet_direction == "RIGHT",self.change_to == "UP" and not self.direction == "DOWN",self.change_to == "DOWN" and not self.direction == "UP")):
            self.movemenet_direction = self.change_to

    def change_head_pos(self):
        if self.movemenet_direction == "RIGHT":
            self.snake_head_position[0] += 10
        elif self.movemenet_direction == "LEFT":
            self.snake_head_position[0] -= 10
        elif self.movemenet_direction == "UP":
            self.snake_head_position[1] -= 10
        elif self.movemenet_direction == "DOWN":
            self.snake_head_position[1] += 10
    def snake_body_movement(self,score,food_pos,scr_width,scr_height):
        self.snake_body.insert(0, list(self.snake_head_position))
        if(self.snake_head_position[0] == food_pos[0] and self.snake_head_position[1] == food_pos[1]):
            food_pos = [random.randrange(1, scr_width/10)*10,random.randrange(1, scr_height/10)*10]
            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos
    def draw_snake(self,play_surface,surface_color):
        play_surface.fill(surface_color)
        for i in self.snake_body:
            pygame.draw.rect(play_surface,self.snake_color,pygame.Rect(i[0],i[1],10,10))

    def check_for_boundaries(self,game_over, scr_width, scr_height):
        if any((self.snake_head_position[0] > scr_width-10 or self.snake_head_position[0] < 0,self.snake_head_position[1] > scr_height-10 or self.snake_head_position[1] < 0)):
            game_over()
        for block in self.snake_body[1:]:
            if (block[0] == self.snake_head_pos[0] and block[1] == self.snake_head_pos[1]):
                game_over()



        


