from sprites.Player import *
from sprites.Weapon import *
from sprites.Cartridges import *
class Game:
    def __init__(self):

        # Создаем игру и окно
        pygame.init()
        # pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("GTA")
        clock = pygame.time.Clock()
        #присвоение спрайтов
        all_sprites = pygame.sprite.Group()
        player = Player()
        weapon = Weapon()
        сartridges = Cartridges()
        all_sprites.add(player, weapon, сartridges)

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
            pygame.sprite.spritecollide(player, weapon, False)
            # Рендеринг
            screen.fill(BLACK)
            all_sprites.draw(screen)
            # После отрисовки всего, переворачиваем экран
            pygame.display.flip()

        pygame.quit()