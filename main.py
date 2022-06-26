import sqlite3
from bs4 import BeautifulSoup
import pygame
import random
import time


#
# with open('eng.html', encoding='utf-8') as file:
#     contents = file.read()
#
# add = []
# countries = []
# capitals = []
# task = 0
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# pygame.init()
# surface = pygame.display.set_mode((800, 800))
# pygame.display.set_caption('Geography')
# font = pygame.font.SysFont('Arial', 66, bold=True)
# fontQuestion = pygame.font.SysFont('Arial', 33, bold=True)
# rect_rounded = pygame.image.load(r'C:\Users\User001\PycharmProjects\geographyCapCount\images\rect_rounded.jpg')
#
con = sqlite3.connect('geography.db')
cur = con.cursor()

cur.execute('''DELETE FROM CapCount WHERE country = 'Амман' ''')
cur.execute('''INSERT INTO CapCount VALUES ('Иордания', 'Амман') ''')
print(list(cur.execute('SELECT * FROM CapCount')))
# addition = list(cur.execute('SELECT * FROM CapCount'))
# dopAdd = addition
# print(len(addition), len(dopAdd))
# print(addition, dopAdd)
#
#
# random_num = random.randint(0, 216)
# renderQuestion = font.render(f'{addition[random_num][0]}', 1, pygame.Color('black'))
# renderQuestion_rect = renderQuestion.get_rect()
# renderQuestion_rect.x, renderQuestion_rect.y = 300, 200
# renderAskRight = fontQuestion.render(f'{addition[random_num][1]}', 1, pygame.Color('black'))
# renderAskRight_rect = renderAskRight.get_rect()
# renderAskRight_rect.x, renderAskRight_rect.y = 50, 450
# dopAdd.pop(random_num)
# addition.pop(random_num)
# random_num_second = random.randint(0, 215)
# renderAskWrong1 = fontQuestion.render(f'{dopAdd[random_num_second][1]}', 1, pygame.Color('black'))
# renderAskWrong1_rect = renderAskWrong1.get_rect()
# renderAskWrong1_rect.x, renderAskWrong1_rect.y = 450, 450
# dopAdd.pop(random_num_second)
# random_num_third = random.randint(0, 214)
# renderAskWrong2 = fontQuestion.render(f'{dopAdd[random_num_third][1]}', 1, pygame.Color('black'))
# renderAskWrong2_rect = renderAskWrong2.get_rect()
# renderAskWrong2_rect.x, renderAskWrong2_rect.y = 50, 650
# dopAdd.pop(random_num_third)
# random_num_fourth = random.randint(0, 213)
# renderAskWrong3 = fontQuestion.render(f'{dopAdd[random_num_fourth][1]}', 1, pygame.Color('black'))
# renderAskWrong3_rect = renderAskWrong3.get_rect()
# renderAskWrong3_rect.x, renderAskWrong3_rect.y = 450, 650
# dopAdd.pop(random_num_fourth)
#
#
# def close():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#
# def start():
#     surface.fill((255, 255, 255))
#     render = font.render(f'Get start', 1, pygame.Color('black'))
#     render_rect = render.get_rect()
#     render_rect.x, render_rect.y = 275, 350
#     surface.blit(render, (275, 350))
#
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONUP:
#             if render_rect.collidepoint(pygame.mouse.get_pos()):
#                 print('OK')
#         if event.type == pygame.QUIT:
#             exit()
#
#
# def questions():
#     surface.fill((255, 255, 255))
#
#     rect_rounded_rect1 = rect_rounded.get_rect()
#     rect_rounded_rect2 = rect_rounded.get_rect()
#     rect_rounded_rect3 = rect_rounded.get_rect()
#     rect_rounded_rect4 = rect_rounded.get_rect()
#
#     rect_rounded_rect1.x, rect_rounded_rect1.y = 0, 400
#     rect_rounded_rect2.x, rect_rounded_rect2.y = 400, 400
#     rect_rounded_rect3.x, rect_rounded_rect3.y = 0, 600
#     rect_rounded_rect4.x, rect_rounded_rect4.y = 400, 600
#
#     surface.blit(rect_rounded, (rect_rounded_rect1.x, rect_rounded_rect1.y))
#     surface.blit(rect_rounded, (rect_rounded_rect2.x, rect_rounded_rect2.y))
#     surface.blit(rect_rounded, (rect_rounded_rect3.x, rect_rounded_rect3.y))
#     surface.blit(rect_rounded, (rect_rounded_rect4.x, rect_rounded_rect4.y))
#
#     if task == 0:
#         surface.blit(renderQuestion, (renderQuestion_rect.x, renderQuestion_rect.y))
#         surface.blit(renderAskRight, (renderAskRight_rect.x, renderAskRight_rect.y))
#         surface.blit(renderAskWrong1, (renderAskWrong1_rect.x, renderAskWrong1_rect.y))
#         surface.blit(renderAskWrong2, (renderAskWrong2_rect.x, renderAskWrong2_rect.y))
#         surface.blit(renderAskWrong3, (renderAskWrong3_rect.x, renderAskWrong3_rect.y))
#
#
# def end():
#     pass
#
#
# while True:
#     start()
#     questions()
#     end()
#
#     # for i in soup.find_all('a'):
#     #     if i.get('title') is not None:
#     #         add.append(i.get('title'))
#     #
#     # for index, j in enumerate(add[4:438]):
#     #     if index % 2 == 0:
#     #         countries.append(j)
#     #     else:
#     #         capitals.append(j)
#     #
#     # cur.execute('''CREATE TABLE CapitalCountries
#     #                 (countryRUS text, capitalRUS text, countryENG text, capitalENG text)''')
#     #
#     # for count, cap in zip(countries, capitals):
#     #     cur.execute(f'''INSERT INTO CapCount VALUES ('{count}', '{cap}')''')
#     #
#     # for row in cur.execute('''SELECT * FROM CapCount'''):
#     #     print(row)
#     #
#     #
#     # con.commit()
#
#     close()
#     pygame.display.update()
con.commit()
