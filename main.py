import sqlite3
from bs4 import BeautifulSoup
import pygame

with open('eng.html', encoding='utf-8') as file:
    contents = file.read()

add = []
countries = []
capitals = []

soup = BeautifulSoup(contents, 'html.parser')

pygame.init()
surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Geography')

con = sqlite3.connect('geography.db')
cur = con.cursor()


def close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


while True:
    surface.fill((255, 255, 255))

    for i in soup.find_all('a'):
        if i.get('title') is not None:
            add.append(i.get('title'))

    for index, j in enumerate(add[4:438]):
        if index % 2 == 0:
            countries.append(j)
        else:
            capitals.append(j)

    # cur.execute('''CREATE TABLE CapitalCountries
    #                 (countryRUS text, capitalRUS text, countryENG text, capitalENG text)''')

    # for count, cap in zip(countries, capitals):
    #     cur.execute(f'''INSERT INTO CapCount VALUES ('{count}', '{cap}')''')
    #
    # for row in cur.execute('''SELECT * FROM CapCount'''):
    #     print(row)
    #
    #
    # con.commit()

    close()
    pygame.display.update()
