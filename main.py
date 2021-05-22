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

        def surface(self):
            self.play_surface = pygame.display.set_mode((self.scr_width,self.scr_height))
            pygame.display.set_caption('Snake')

        def event_loop(self,change_to):

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
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

        


