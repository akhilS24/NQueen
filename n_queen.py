import backtrack_algo
import pygame as pg
import numpy as np

pg.init()


class Grid:
    def __init__(self, n):
        self.dim=n
    def draw_grid(self, window):
        for i in range(0, 801, 800//self.dim):
            pg.draw.line(window, (255,255,255), (0, i), (800, i), 1)
            pg.draw.line(window, (255, 255, 255), (i, 0), (i, 800), 1)

class Queens:
    def _init__(self, n):
        self.queen_num=n

def main():

    #instantiating th grid class
    grid_num=input("Enter the dimension: ")
    for digit in grid_num:
        run = False if not digit.isdigit() else True
    if run:
        grid_num=int(grid_num)
        grid = Grid(grid_num)

        #creating the pygame window
        WIN = (800, 800)
        window = pg.display.set_mode(WIN)
    print(type(grid_num))
    #pygame loop
    while run:
        window.fill((0,0,0))
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()

        grid.draw_grid(window)
        pg.display.update()

if __name__ == "__main__":
    main()

