import time

import pygame.sprite
from MapGenerator.WebGenerator import WebGenerator
from sprites.Player import *
from sprites.Backpack import *
from MapGenerator.WebGenerator import *
from sprites.Zombie import *
from sprites.NLO import *
class Game:
    def __init__(self):

        # Создаем игру и окно
        pygame.init()
        #pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("****")
        clock = pygame.time.Clock()
        #присвоение спрайтов
        all_sprites = pygame.sprite.Group()
        map_group = pygame.sprite.Group()
        zombie_group = pygame.sprite.Group()
        zombie = Zombie()
        backpack = Backpack()
        player = Player()
        f1 = pygame.font.Font(None, 70)
        self.text1 = f1.render('', True,RED)

        web = WebGenerator().createWeb
        map_group.add(web)

        # for row in web:
        #     #
        #     for cell in row:
                #print('game', cell.rect.x, cell.rect.y)
                # map_group.add(cell)
        zombie_group.add(zombie)
        all_sprites.add(player,  backpack.сartridges_group, backpack.weapon_group,zombie_group,
                        backpack.ammunition_group)
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # левая кнопка мыши
                        x2,y2 = event.pos
                        nlo = NLO(x1=player.rect.x, y1=player.rect.y,x2=x2,y2=y2,damage=3)
                        all_sprites.add(nlo)
                        nlo_grop = pygame.sprite.Group()
                        nlo_grop.add(nlo)
                        if abs(nlo.rect.x - x2) < 50  or abs(nlo.rect.y - y2) < 50:
                            nlo.kill()
            # Обновление
            all_sprites.update()
            map_group.update()

            self.text2 = f1.render("HP: "+str(player.h_p), True,RED)
            self.text3 = f1.render("пули: "+str(player.cat_amount), True, GREEN)
            сartridges_collision = pygame.sprite.spritecollide(player, backpack.сartridges_group, True)
            zombies_collision = pygame.sprite.spritecollide(player, zombie_group, False)
            weapon_collision = pygame.sprite.spritecollide(player, backpack.weapon_group, True)
            ammunition_collision = pygame.sprite.spritecollide(player, backpack.ammunition_group, True)
            if len(сartridges_collision) >= 1:
                player.cat_amount += 7
            if len(zombies_collision) >= 1:
                player.h_p -= 1
                player.rect.y -= player.speedy + 20
                player.rect.x -= player.speedx +20
                if player.h_p <= 0:
                    player.kill()
                    self.text1 = f1.render('ВЫ ПРОИГРАЛИ!', True,RED)
            if player.again == 1:
                web = WebGenerator().createWeb
                map_group.empty()
                map_group.add(web)
                backpack.ammunition.kill()
                backpack.weapon.kill()
                backpack.сartridges.kill()
                zombie.kill()
                if random.randint(0,1) == 0:
                    zombie_group.add(zombie)
                    all_sprites.add(zombie_group)
                    zombie.moveToRandomPoint()
                if random.randint(0,3) == 0:
                    backpack.сartridges_group.add(backpack.сartridges)
                    all_sprites.add(backpack.сartridges)
                    backpack.сartridges.moveToRandomPoint()
                if random.randint(0,3) == 0:
                    backpack.Random_ammunitions()
                    backpack.ammunition_group.add(backpack.ammunition)
                    all_sprites.add(backpack.ammunition)
                    backpack.ammunition.moveToRandomPoint()
                if random.randint(0,6) == 0:
                    backpack.Random_weapon()
                    backpack.weapon_group.add(backpack.weapon)
                    all_sprites.add(backpack.weapon)
                    backpack.weapon.moveToRandomPoint()
                player.again = 0
           # if hits:
            #   running = False

            # Рендеринг
            screen.fill(BLACK)
            map_group.draw(screen)
            all_sprites.draw(screen)
            screen.blit(self.text1, (WIDTH / 2, HEIGHT / 2))
            screen.blit(self.text2, (60,60))
            screen.blit(self.text3, (60, 120))

            # После отрисовки всего, переворачиваем экран
            pygame.display.flip()

        pygame.quit()