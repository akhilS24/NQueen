from backtrack_algo import Backtracking
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

    def __init__(self, n):
        self.queen_num=n
        self.x = 0
        self.y = 0
    def draw_queen(self, window, grid_num):
        pg.draw.circle(window, (255, 0, 0), (int((800//grid_num)*(self.queen_num+(1/2))), int((800//grid_num)*(self.y+(1/2)))), 20, 0)




def main():


    grid_num=input("Enter the dimension: ")
    for digit in grid_num:
        run = False if not digit.isdigit() else True
    if run:
        grid_num=int(grid_num)

        # instantiating th grid class
        grid = Grid(grid_num)

        #intantiating the queen class
        queen = []
        for i in range(grid_num):
            queen.append(Queens(i))

        #creating a 2D array
        array = np.zeros([grid_num, grid_num])
        status = True
        occupied = []


        #creating the pygame window
        WIN = (800, 800)
        window = pg.display.set_mode(WIN)

    Backtracking(array, 0, status, grid_num, occupied, queen)
    #pygame loop
    while run:
        window.fill((0,0,0))
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()



        grid.draw_grid(window)
        for i in range(grid_num):
            queen[i].draw_queen(window, grid_num)
        pg.display.update()



if __name__ == "__main__":
    main()

