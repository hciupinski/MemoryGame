import pygame, sys, random
from pygame.locals import *


class Memory(object):

    def __init__(self):
        #
        pygame.init()
        self.board = Board()
        self.fps_clock = pygame.time.Clock()
        self.board.draw()
        self.move = 1
        self.choice_1 = None
        self.choice_2 = None
        self.pos_1 = None
        self.pos_2 = None
        self.hit = 0
        self.score = 0

    def game_loop(self):
        # while True: event
        while not self.handle_events():
            # act in a loop until receiving the signal to quit()
            self.fps_clock.tick(15)

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                pole = self.board.cards
                for pos in pole:
                    if pos.collidepoint(x, y):
                        if self.move == 1:
                            self.pos_1 = pos
                            self.choice_1 = self.board.unhide(pos)
                            print(f'choice 1: {self.choice_1}')
                            self.move += 1
                        elif self.move == 2:
                            self.score += 1
                            self.pos_2 = pos
                            self.choice_2 = self.board.unhide(pos)
                            print(f'choice 2: {self.choice_2}')

                            if self.choice_1 == self.choice_2:
                                print("hit")
                                self.pos_1, self.pos_2 = None, None
                                self.move = 1
                                self.hit += 1
                            else:
                                self.move = 1
                                self.board.hide(self.pos_1)
                                self.board.hide(self.pos_2)

            if self.hit == 8:
                print(f'You finished the game in {self.score} steps.')
                pygame.quit()


class Board(object):

    def __init__(self):
        # rysowanie okna gry, utworz Surface dla Gry, utworz Surface dla tabeli wynikow, utworz Array 4x4
        self.width = 370
        self.height = 370
        self.surface = pygame.display.set_mode((self.width, self.height), 0, 32)
        pygame.display.set_caption('MemoryGame by Trebuh')
        self.cards = []
        self.blank_cards = []
        self.pictures = {}
        self.screen = pygame.display.get_surface()
        self.blank = pygame.image.load('pictures/0.png')

    def draw(self, *args):
        self.load_pictures()
        self.shuffle_card(self.pictures)
        self.draw_card()

        for drawable in args:
            drawable.draw_on(self.surface)

        pygame.display.flip()

    def draw_card(self):
        i, x, y = 0, 0, 0

        for x in range(4):
            for y in range(4):
                w = x * 90 + 10
                h = y * 90 + 10
                self.cards.append(self.screen.blit(self.pictures[i][1], (w, h)))
                self.blank_cards.append(self.screen.blit(self.blank, (w, h)))
                i += 1

    def shuffle_card(self, pictures):
        random.shuffle(pictures)
        return pictures

    def load_pictures(self):
        x = 0
        for i in range(8):
            for j in range(2):
                self.pictures[x] = (i, pygame.image.load('pictures/' + str(i + 1) + '.png'))
                x += 1

        return self.pictures

    # def del_hit_cards(self, pos_1, pos_2):
    #     id_1 = self.cards.index(pos_1)
    #     id_2 = self.cards.index(pos_2)

    def unhide(self, pos):
        id = self.cards.index(pos)
        pict = self.screen.blit(self.pictures[id][1], pos)
        # pict2 = self.blank.set_alpha(255)
        print(f'unhide -> cards.index:{id}, pictures:{self.pictures[id][0]}')  # self.pictures[id]
        pygame.display.update()
        return self.pictures[id][0]

    def hide(self, pos):
        bl = self.screen.blit(self.blank, pos)
        # pygame.display.update()


# def score_table(self):
# wypisz wyniki z pliku

# def check_win(unhide):
# sprawdz czy wszystko odsloniete


if __name__ == "__main__":
    game = Memory()
    game.game_loop()
