import pygame.sprite

from sprites.Player import *
from sprites.Weapon import *
from sprites.Cartridges import *
from sprites.Backpack import *
from MapGenerator.WebGenerator import *
class Game:
    def __init__(self):

        # Создаем игру и окно
        pygame.init()
        #pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("GTA")
        clock = pygame.time.Clock()
        #присвоение спрайтов
        all_sprites = pygame.sprite.Group()
        map_group = pygame.sprite.Group()

        backpack = Backpack()
        player = Player()

        web = WebGenerator().createWeb
        map_group.add(web)

        # for row in web:
        #     #
        #     for cell in row:
                #print('game', cell.rect.x, cell.rect.y)
                # map_group.add(cell)

        all_sprites.add(player,  backpack.сartridges_group, backpack.weapon_group)
        # Цикл игры
        running = True
        while running:
            # Держим цикл на правильной скорости
            clock.tick(FPS)


            # Ввод процесса (события)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False

            # Обновление
            all_sprites.update()
            map_group.update()

            сartridges_collision = pygame.sprite.spritecollide(player, backpack.сartridges_group, True)

            weapon_collision = pygame.sprite.spritecollide(player, backpack.weapon_group, True)
            if player.new == 1:
                if random.randint(0,3) == 0:
                    player.new = 0
                    all_sprites.add(backpack.сartridges)
                    backpack.сartridges_group.add(backpack.сartridges)
                    backpack.сartridges.moveToRandomPoint()
                if random.randint(0,7) == 0:
                    player.new = 0
                    all_sprites.add(backpack.weapon)
                    backpack.weapon_group.add(backpack.weapon)
                    backpack.weapon.moveToRandomPoint()

           # if hits:
            #   running = False

            # Рендеринг
            screen.fill(BLACK)
            map_group.draw(screen)
            all_sprites.draw(screen)

            # После отрисовки всего, переворачиваем экран
            pygame.display.flip()

        pygame.quit()