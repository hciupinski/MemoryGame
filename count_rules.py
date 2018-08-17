import random

cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
cards_pos = []
pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


for i in range(8):
    for j in range(2):
        cards_pos.append(cards[i])

random.shuffle(cards_pos)

event = len(cards)
moves = 0
while event > 0:
    x = random.choice(pos)
    choice_1 = cards_pos[x]
    t_pos = pos[:]
    t_pos.remove(x)
    y = random.choice(t_pos)
    choice_2 = cards_pos[y]
    moves += 1
    print(choice_1+" "+choice_2)
    if choice_1 == choice_2:
        print("Trafione")
        event -=1
        pos.remove(x)
        pos.remove(y)


print("Liczba wszystkich ruchów: "+str(moves))

# while end == False:
#
#     if move == 1:
#         if event.type == pygame.locals.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()
#             pole = self.board.cards_pos
#             for pos in pole:
#                 if pos.collidepoint(x, y):
#                     t_pos = pos
#                     choice_1 = self.board.unhide(pos)
#                     pygame.display.update()
#                     move+=1
#     elif move == 2:
#         if event.type == pygame.locals.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()
#             pole = self.board.cards_pos
#             for pos in pole:
#                 if pos.collidepoint(x, y):
#                     choice_2 = self.board.unhide(pos)
#                     pygame.display.update()
#         if choice_1 == choice_2:
#             print("trafione")
#         else:
#             move = 1
#             self.hide(pos)
#             self.hide(t_pos)
