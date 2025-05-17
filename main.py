import pygame
import random
from game.sprites import Player, Enemy, Bullet


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Run and Gun")
    clock = pygame.time.Clock()

    player = Player((100, 540))
    player_group = pygame.sprite.Group(player)
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    enemy_timer = 0
    running = True
    while running:
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.shoot(bullets)

        # Spawn enemies periodically
        enemy_timer += 1
        if enemy_timer > 60:
            enemy_timer = 0
            enemy_pos = (800, 540)
            enemy = Enemy(enemy_pos)
            enemies.add(enemy)

        # Update sprites
        player_group.update(keys_pressed)
        enemies.update()
        bullets.update()

        # Collision detection
        for bullet in pygame.sprite.groupcollide(bullets, enemies, True, True):
            pass  # bullet and enemy disappear
        if pygame.sprite.spritecollide(player, enemies, False):
            running = False

        # Drawing
        screen.fill((135, 206, 235))  # sky blue background
        player_group.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
