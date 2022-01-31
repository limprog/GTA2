import time
import pygame.sprite
from MapGenerator.WebGenerator import WebGenerator
from sprites.Inventory import Inventory
from sprites.Player import *
from sprites.Backpack import *
from MapGenerator.WebGenerator import *
from sprites.Zombie import *
from sprites.NLO import *
from sprites.pig import *


class Game:
    def __init__(self):

        # Создаем игру и окно
        pygame.init()
        # pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("****")
        clock = pygame.time.Clock()
        # присвоение спрайтов
        all_sprites = pygame.sprite.Group()
        map_group = pygame.sprite.Group()
        zombie_group = pygame.sprite.Group()
        nlo_group = pygame.sprite.Group()
        pig_group = pygame.sprite.Group()
        zombie = Zombie()
        backpack = Backpack()
        player = Player()
        pig = Pig()
        inventory = Inventory(player, 10, 5, 2)

        f2 = pygame.font.Font(None, 30)
        f1 = pygame.font.Font(None, 70)
        self.text7 = f2.render(str(pig.hp), True, WHITE)
        self.text4 = f2.render(str(zombie.hp), True, WHITE)
        self.text1 = f1.render('', True, RED)
        web = WebGenerator().createWeb
        map_group.add(web)

        # for row in web:
        #     #
        #     for cell in row:
        # print('game', cell.rect.x, cell.rect.y)
        # map_group.add(cell)
        zombie_group.add(zombie)
        pig_group.add(pig)
        all_sprites.add(player, backpack.сartridges_group, backpack.weapon_group, zombie_group,
                        backpack.ammunition_group, pig)
        # Цикл игры
        running = True
        while running:
            # Держим цикл на правильной скорости
            clock.tick(FPS)
            screen.fill(BLACK)
            map_group.draw(screen)

            # Ввод процесса (события)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        inventory.toggleInventory()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if inventory.display_inventory:
                        mouse_pos = pygame.mouse.get_pos()
                        inventory.checkSlot(screen, mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if inventory.display_inventory:
                        inventory.moveItem(screen)
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if inventory.display_inventory:
                        inventory.placeItem(screen)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # левая кнопка мыши
                        x2, y2 = event.pos
                        if player.clip >= 1:
                            player.clip -= 1
                            nlo = NLO(x1=player.rect.x, y1=player.rect.y, x2=x2, y2=y2, damage=3)
                            all_sprites.add(nlo)
                            nlo_group.add(nlo)
                        else:
                            pass

            for nlo_elem in nlo_group:
                if abs(nlo_elem.rect.x - nlo_elem.x2) < 25 and abs(nlo_elem.rect.y - nlo_elem.y2) < 25:
                    nlo_elem.kill()
            # Обновление
            all_sprites.update()
            map_group.update()
            self.text6 = f1.render("Монеты: " + str(player.conin), True, GREEN)
            self.text2 = f1.render("HP: " + str(player.hp), True, RED)
            self.text3 = f1.render("Патроны: " + str(player.cat_amount), True, GREEN)
            self.text5 = f1.render('Магазин: ' + str(player.clip), True, RED)

            ### Проверить эффективность! Не замедляет ли.
            сartridges_collision = pygame.sprite.spritecollide(player, backpack.сartridges_group, True)
            zombies_collision = pygame.sprite.spritecollide(player, zombie_group, False)

            weapon_collision = pygame.sprite.spritecollide(player, backpack.weapon_group, True)
            ammunition_collision = pygame.sprite.spritecollide(player, backpack.ammunition_group, True)

            kill_zombie_collisions = pygame.sprite.groupcollide(zombie_group, nlo_group, False, True)
            kill_pig_collisions = pygame.sprite.groupcollide(pig_group, nlo_group, False, True)

            pig_eat_collision = pygame.sprite.spritecollide(player, pig_group, False)

            for kill_pig_collision in kill_pig_collisions.items():
                kill_pig_collision[0].hp -= player.damage
                self.text7 = f2.render(str(kill_pig_collision[0].hp), True, WHITE)
                if kill_pig_collision[0].hp <= 0:
                    self.text7 = f2.render(str(kill_pig_collision[0].hp), True, WHITE)
                    pig.updat = 0

            if len(weapon_collision) >= 1:
                inventory.addItemInv(weapon_collision[0])

            if len(ammunition_collision) >= 1:
                inventory.addItemInv(ammunition_collision[0])

            if len(pig_eat_collision) >= 1:
                if pig.updat == 0:
                    player.hp += 2
                    self.text2 = f1.render(str(player.hp), True, WHITE)
                    pig.updat = 1
                    pig.kill()
                else:
                    player.hp -= 1
            if len(сartridges_collision) >= 1:
                player.cat_amount += 7
            if len(zombies_collision) >= 1:
                player.hp -= 1
                player.rect.y -= player.speedy + 20
                player.rect.x -= player.speedx + 20
            for kill_zombie_collision in kill_zombie_collisions.items():
                kill_zombie_collision[0].hp -= player.damage
                self.text4 = f2.render(str(kill_zombie_collision[0].hp), True, WHITE)
                if kill_zombie_collision[0].hp <= 0:
                    self.text4 = f2.render('', True, WHITE)
                    kill_zombie_collision[0].kill()
                    player.conin += 1
            if player.hp <= 0:
                player.kill()
                self.text1 = f1.render('ВЫ ПРОИГРАЛИ!', True, RED)
            if player.again == 1:
                web = WebGenerator().createWeb
                map_group.empty()
                map_group.add(web)
                backpack.ammunition.kill()
                backpack.weapon.kill()
                backpack.сartridges.kill()
                zombie.kill()
                self.text4 = f2.render('', True, WHITE)
                if random.randint(0, 3):
                    pig.hp = 10
                    pig_group.add(pig)
                    all_sprites.add(pig)
                    pig.moveToRandomPoint()
                    self.text7 = f2.render(str(pig.hp), True, WHITE)
                if random.randint(0, 1) == 0:
                    zombie.hp = 20
                    zombie_group.add(zombie)
                    all_sprites.add(zombie_group)
                    zombie.moveToRandomPoint()
                    self.text4 = f2.render(str(zombie.hp), True, WHITE)
                if random.randint(0, 3) == 0:
                    backpack.сartridges_group.add(backpack.сartridges)
                    all_sprites.add(backpack.сartridges)
                    backpack.сartridges.moveToRandomPoint()
                if random.randint(0, 3) == 0:
                    backpack.Random_ammunitions()
                    backpack.ammunition_group.add(backpack.ammunition)
                    all_sprites.add(backpack.ammunition)
                    backpack.ammunition.moveToRandomPoint()
                if random.randint(0, 6) == 0:
                    backpack.Random_weapon()
                    backpack.weapon_group.add(backpack.weapon)
                    all_sprites.add(backpack.weapon)
                    backpack.weapon.moveToRandomPoint()
                player.again = 0
            # if hits:
            #   running = False

            # Рендеринг

            all_sprites.draw(screen)
            inventory.draw(screen)
            screen.blit(self.text1, (WIDTH / 2, HEIGHT / 2))
            screen.blit(self.text2, (60, 60))
            screen.blit(self.text3, (60, 120))
            screen.blit(self.text4, (zombie.rect.x, zombie.rect.y))
            screen.blit(self.text5, (60, 180))
            screen.blit(self.text6, (60, 240))
            screen.blit(self.text7, (pig.rect.x, pig.rect.y))

            # После отрисовки всего, переворачиваем экран
            pygame.display.flip()

        pygame.quit()
