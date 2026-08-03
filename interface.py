import pygame as pg

# COLORS #

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BACKGROUND_COLOR = BLACK
BRUSH_COLOR = WHITE

pg.init()
CANVAS_SIZE = 280
BRUSH_RADIUS = 16

screen = pg.display.set_mode((CANVAS_SIZE, CANVAS_SIZE))
pg.display.set_caption("Drawing Interface")
clock = pg.time.Clock()

screen.fill(BACKGROUND_COLOR)

drawing = False
last_pos = None

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            last_pos = event.pos
            pg.draw.circle(screen, BRUSH_COLOR, event.pos, BRUSH_RADIUS)

        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            last_pos = None

        elif event.type == pg.MOUSEMOTION and drawing:
            current_pos = event.pos
            if last_pos:
                pg.draw.line(screen, BRUSH_COLOR, last_pos, current_pos, BRUSH_RADIUS * 2)
                pg.draw.circle(screen, BRUSH_COLOR, current_pos, BRUSH_RADIUS)
            last_pos = current_pos

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                screen.fill(BACKGROUND_COLOR) 

    pg.display.flip()
    clock.tick(60)

pg.quit()