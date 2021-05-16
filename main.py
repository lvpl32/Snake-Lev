import pygame

pygame.init()

win_size = 700
win = pygame.display.set_mode((win_size,win_size))
background_color = (0,0,0)

font = pygame.font.SysFont('arial', 32)

def draw_text(text,font,color,frame,x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    frame.blit(textobj,textrect)


def draw_grid(win_size):
    for i in range(0, win_size, 50):
        pygame.draw.line(win, (255,255,255), (0,i), (win_size, i))
        pygame.draw.line(win, (255,255,255), (i,0), (i, win_size))


menu_color = (0,0,0)

def menu(win):
    running = True
    events = pygame.event.get()
    while running:
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        win.fill(menu_color)
        pygame.display.update()
        




while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu(win)

    draw_text('Menu', font, (255,0,0), win, 300,300)
    draw_grid(700)


    win.fill(background_color)
    pygame.display.update()
