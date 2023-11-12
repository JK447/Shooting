import pygame
import random

# 初期化
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# プレイヤー設定
player_img = pygame.Surface((50, 30))
player_img.fill((0, 255, 0))
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 50))

# 敵設定
enemy_img = pygame.Surface((30, 30))
enemy_img.fill((255, 0, 0))
enemies = []

# 弾丸設定
bullet_img = pygame.Surface((5, 10))
bullet_img.fill((255, 255, 255))
bullets = []

# プレイヤーの動き
def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5

# 弾丸の動き
def move_bullets():
    for bullet in bullets:
        bullet.y -= 5
        if bullet.top < 0:
            bullets.remove(bullet)

# 敵の生成
def create_enemy():
    rect = enemy_img.get_rect(center=(random.randint(0, WIDTH), 0))
    enemies.append(rect)

# 敵の動き
def move_enemies():
    for enemy in enemies:
        enemy.y += 2
        if enemy.bottom > HEIGHT:
            enemies.remove(enemy)

# 衝突検出
def check_collisions():
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(bullet_img.get_rect(midbottom=player_rect.midtop))

    move_player()
    move_bullets()
    if random.randint(1, 30) == 1:
        create_enemy()
    move_enemies()
    check_collisions()

    screen.fill((0, 0, 0))
    screen.blit(player_img, player_rect)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
