import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 30, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.height = self.life.rows * cell_size
        self.width = self.life.cols * cell_size
        self.screen_size = self.life.cols * cell_size, self.life.rows * cell_size
        self.screen = pygame.display.set_mode(self.screen_size)
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))
        pass

    def draw_grid(self) -> None:
        for y in range(self.life.rows):
            for x in range(self.life.cols):
                if self.grid[y][x] == 0:
                    # белый
                    COLOR = [255, 255, 255]
                else:
                    # зелёный
                    COLOR = [0, 255, 0]
                pygame.draw.rect(self.screen,
                                 COLOR,
                                 (
                                     x * self.cell_size + 1,
                                     y * self.cell_size + 1,
                                     self.cell_size - 1,
                                     self.cell_size - 1
                                 )
                                 )
        pass

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        self.is_pause = False

        # Создание списка клеток
        self.grid = self.life.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # при нажатии на пробел можно поставить или снять паузу
                    if event.key == pygame.K_SPACE:
                        self.is_pause = not self.is_pause
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # левой кнопкой мыши можно заполнять или очищать ячейки
                    if event.button == 1:
                        cell = grid[event.pos[1] // self.cell_size][event.pos[0] // self.cell_size]
                        cell = 1 if cell == 0 else 0
                        grid[event.pos[1] // self.cell_size][event.pos[0] // self.cell_size] = cell

                if event.type == QUIT:
                    running = False
            # Если стоит пауза, игра как бы продолжается, но показывается одно поколение
            if self.is_pause:
                self.draw_lines()
                self.draw_grid()
            else:
                grid = self.life.get_next_generation()
                self.draw_lines()
                self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

def main():
    game = GameOfLife(size=(25, 25))
    app = GUI(game)
    app.run()

if __name__ == '__main__':
    main()