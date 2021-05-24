import sys
import pygame
import constants as con
import draw_something
import db_managing as db

#Всплывающее меню
def draw_menu(frame, result):
    frame.fill(con.black)
    draw_something.draw_text('Menu', con.menu_font, con.green,
    frame, 210, 50)
    draw_something.draw_text('Current score: ' + str(result),
    con.list_font, con.blue, frame, 100, 150)
    draw_something.draw_text('Your best result: ' + str(db.your_best_result()),
    con.list_font, con.blue, frame, 100, 200)
    draw_something.draw_text('Your username: ' + db.get_username(),
    con.list_font, con.blue, frame, 100, 250)
    draw_something.draw_text('Your average score: ' + str(db.your_average()),
    con.list_font, con.blue, frame, 100, 300)
    draw_something.draw_text('All time best score: ' + str(db.best_result()),
    con.list_font, con.blue, frame, 100, 350)
    mx, my = pygame.mouse.get_pos()
    button_reset = pygame.Rect(175, 400, 150, 50)
    if button_reset.collidepoint((mx,my)):
        db.db_reset()
    pygame.draw.rect(frame, con.red, button_reset)
    draw_something.draw_text('Reset results',
    con.list_font, con.white, frame, 185, 415)

def start_menu(frame, clock, result):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        draw_menu(frame, result)
        pygame.display.update()
        clock.tick(23)