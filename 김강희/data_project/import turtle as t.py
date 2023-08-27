import pygame
from pygame.locals import *
import os
import sys
import random

os.environ["SDL_VIDEO_CENTERED"] = "1"

cur_path = os.getcwd()
print("CURPATH:", cur_path)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

FPS = 30

GROUND_HEIGHT = SCREEN_HEIGHT - 70

PLAY_GAME = True


pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Run")

clock = pygame.time.Clock()


jump_sound = pygame.mixer.Sound(cur_path + "\김강희\sound\jump.ogg")
score_sound = pygame.mixer.Sound(cur_path + "\김강희\sound\score.ogg")
game_over_sound = pygame.mixer.Sound(cur_path + "\김강희\sound\game_over.ogg")


def draw_text(text, font_name, size, text_color, position_x, position_y, position):
    font = pygame.font.Font(font_name, size)

    text_plane = font.render(text, True, text_color)
    text_rect = text_plane.get_rect()

    if position == "midtop":
        text_rect.midtop = (int(position_x), int(position_y))
    elif position == "topright":
        text_rect.topright = (int(position_x), int(position_y))

    window.blit(text_plane, text_rect)


def load_image(path, size_x=0, size_y=0):
    image = pygame.image.load(path).convert_alpha()

    if size_x > 0 and size_y > 0:
        image = pygame.transform.scale(image, (size_x, size_y))

    return image, image.get_rect()


def load_sprites(image_path, image_name_prefix, number_of_image, size_x=0, size_y=0):
    images = []

    for i in range(0, number_of_image):
        path = image_path + image_name_prefix + str(i) + ".png"
        image = pygame.image.load(path).convert_alpha()
        if size_x > 0 and size_y > 0:
            image = pygame.transform.scale(image, (size_x, size_y))

        images.append(image)

    return images


class Background:
    def __init__(self, image_path, speed=10):
        self.image0, self.rect0 = load_image(image_path, 1280, 720)
        self.image1, self.rect1 = load_image(image_path, 1280, 720)

        self.rect0.bottom = SCREEN_HEIGHT
        self.rect1.bottom = SCREEN_HEIGHT

        self.rect1.left = self.rect0.right

        self.speed = speed

    def draw(self):
        window.blit(self.image0, self.rect0)
        window.blit(self.image1, self.rect1)

    def update(self):
        self.rect0.left -= int(self.speed)
        self.rect1.left -= int(self.speed)

        if self.rect0.right < 0:
            self.rect0.left = self.rect1.right

        if self.rect1.right < 0:
            self.rect1.left = self.rect0.right


class AllBackgrounds:
    def __init__(self, game_speed):
        self.background_0 = Background(
            cur_path + "\\김강희\\image\\background\\bg_0.png", game_speed
        )
        self.background_1 = Background(
            cur_path + "\\김강희\\image\\background\\bg_1.png", game_speed - 12
        )
        self.background_2 = Background(
            cur_path + "\\김강희\\image\\background\\bg_2.png", game_speed - 13
        )
        self.background_3 = Background(
            cur_path + "\\김강희\\image\\background\\bg_3.png", game_speed - 14
        )

    def update_speed(self, speed):
        self.background_0.speed = speed
        self.background_1.speed = speed - 12
        self.background_2.speed = speed - 13
        self.background_3.speed = speed - 14

    def draw(self):
        self.background_3.draw()
        self.background_2.draw()
        self.background_1.draw()
        self.background_0.draw()

    def update(self):
        self.background_3.update()
        self.background_2.update()
        self.background_1.update()
        self.background_0.update()


# class Coin:
#     def __init__(self, speed=10):
#         self.coin_images = load_sprites("image/score/", "coins_", 5, 160, 160)

#         self.coin_images_0, self.rect_0 = (
#             self.coin_images[0],
#             self.coin_images[0].get_rect(),
#         )
#         self.coin_image_1, self.rect_1 = (
#             self.coin_images[1],
#             self.coin_images[1].get_rect(),
#         )

#         self.rect_0.bottom = GROUND_HEIGHT - 20
#         self.rect_0.left = SCREEN_WIDTH

#         self.rect_1.bottom = GROUND_HEIGHT - 20
#         self.rect_1.left = self.rect_0.right + int(SCREEN_WIDTH / 2)

#         self.speed = speed

#         self.range_0 = 240
#         self.range_1 = 720

#     def get_coin(self):
#         current_coin = [self.coin_images_0, self.coin_image_1]
#         coin_rect = [self.rect_0, self.rect_1]

#         return current_coin, coin_rect

#     def update_speed(self, speed):
#         self.speed = speed
#         self.range_0 += 1
#         self.range_1 += 1

#     def draw(self):
#         window.blit(self.coin_image_0, self.rect_0)
#         window.blit(self.coin_image_1, self.rect_1)

#     def update(self):
#         self.rect_0.left -= int(self.speed)
#         self.rect_1.left -= int(self.speed)

#         if self.rect_0.right < 0:
#             temp_position = self.rect_1.right + random.randrange(
#                 self.range_0, self.range_1
#             )

#             if temp_position > SCREEN_WIDTH:
#                 self.rect_0.left = temp_position
#             else:
#                 self.rect_0.left = SCREEN_WIDTH

#             temp_index = random.randrange(0, 5)
#             self.coin_image_0 = self.coin_images[temp_index]

#         if self.rect_1.right < 0:
#             temp_position = self.rect_0.right + random.randrange(
#                 self.range_0, self.range_1
#             )

#             if temp_position > SCREEN_WIDTH:
#                 self.rect_1.left = temp_position
#             else:
#                 self.rect_1.left = SCREEN_WIDTH

#             temp_index = random.randrange(0, 5)
#             self.coin_image_1 = self.coin_images[temp_index]


class Cactus:
    def __init__(self, speed=10):
        self.cactus_images = load_sprites(
            cur_path + "\image\cactus\cactus_", 5, 160, 160
        )

        self.cactus_image_0, self.rect_0 = (
            self.cactus_images[0],
            self.cactus_images[0].get_rect(),
        )
        self.cactus_image_1, self.rect_1 = (
            self.cactus_images[1],
            self.cactus_images[1].get_rect(),
        )

        self.rect_0.bottom = GROUND_HEIGHT - 11
        self.rect_0.left = SCREEN_WIDTH

        self.rect_1.bottom = GROUND_HEIGHT - 11
        self.rect_1.left = self.rect_0.right + int(SCREEN_WIDTH / 2)

        self.speed = speed

        self.range_0 = 240
        self.range_1 = 720

    def get_cactus(self):
        current_cactus = [self.cactus_image_0, self.cactus_image_1]
        cactus_rect = [self.rect_0, self.rect_1]

        return current_cactus, cactus_rect

    def update_speed(self, speed):
        self.speed = speed
        self.range_0 += 1
        self.range_1 += 1

    def draw(self):
        window.blit(self.cactus_image_0, self.rect_0)
        window.blit(self.cactus_image_1, self.rect_1)

    def update(self):
        self.rect_0.left -= int(self.speed)
        self.rect_1.left -= int(self.speed)

        if self.rect_0.right < 0:
            temp_position = self.rect_1.right + random.randrange(
                self.range_0, self.range_1
            )

            if temp_position > SCREEN_WIDTH:
                self.rect_0.left = temp_position
            else:
                self.rect_0.left = SCREEN_WIDTH

            temp_index = random.randrange(0, 5)
            self.cactus_image_0 = self.cactus_images[temp_index]

        if self.rect_1.right < 0:
            temp_position = self.rect_0.right + random.randrange(
                self.range_0, self.range_1
            )

            if temp_position > SCREEN_WIDTH:
                self.rect_1.left = temp_position
            else:
                self.rect_1.left = SCREEN_WIDTH

            temp_index = random.randrange(0, 5)
            self.cactus_image_1 = self.cactus_images[temp_index]


class Dino:
    def __init__(self):
        self.idle_images = load_sprites("image/dino/", "idle_", 10, 130, 260)
        self.running_images = load_sprites("image/dino/", "run_", 8, 150, 240)
        self.jumping_images = load_sprites("image/dino/", "jump_", 16, 150, 240)

        self.rect = self.idle_images[0].get_rect()

        self.rect.bottom = GROUND_HEIGHT
        self.rect.left = 70

        self.jump_limit = GROUND_HEIGHT - 290
        self.jump_speed = 50
        self.gravity_up = 4
        self.gravity_down = 2

        self.idle_index = 0
        self.running_index = 0
        self.jumping_index = 0

        self.idle = True
        self.running = False
        self.jumping = False
        self.falling = False

        self.call_count = 0

    def check_collision(self, all_cactus):
        if self.running:
            dino_mask = pygame.mask.from_surface(
                self.running_images[self.running_index]
            )
        elif self.jumping:
            dino_mask = pygame.mask.from_surface(
                self.jumping_images[self.jumping_index]
            )
        else:
            dino_mask = pygame.mask.from_surface(self.idle_images[self.idle_index])

        current_cactus, cactus_rect = all_cactus

        offset_0 = (
            cactus_rect[0].left - self.rect.left,
            cactus_rect[0].top - self.rect.top,
        )
        offset_1 = (
            cactus_rect[1].left - self.rect.left,
            cactus_rect[1].top - self.rect.top,
        )

        collide = dino_mask.overlap(
            pygame.mask.from_surface(current_cactus[0]), offset_0
        ) or dino_mask.overlap(pygame.mask.from_surface(current_cactus[1]), offset_1)

        return collide

    def check_coin_collision(self, all_coin):
        if self.running:
            dino_mask = pygame.mask.from_surface(
                self.running_images[self.running_index]
            )
        elif self.jumping:
            dino_mask = pygame.mask.from_surface(
                self.jumping_images[self.jumping_index]
            )
        else:
            dino_mask = pygame.mask.from_surface(self.idle_images[self.idle_index])

        current_coin, coin_rect = all_coin

        offset_0 = (
            coin_rect[0].left - self.rect.left,
            coin_rect[0].top - self.rect.top,
        )
        offset_1 = (
            coin_rect[1].left - self.rect.left,
            coin_rect[1].top - self.rect.top,
        )

        collide = dino_mask.overlap(
            pygame.mask.from_surface(current_coin[0]), offset_0
        ) or dino_mask.overlap(pygame.mask.from_surface(current_coin[1]), offset_1)

        return collide

    def draw(self):
        if self.running:
            window.blit(self.running_images[self.running_index], self.rect)
        elif self.jumping:
            window.blit(self.jumping_images[self.jumping_index], self.rect)
        elif self.idle:
            window.blit(self.idle_images[self.idle_index], self.rect)

    def update(self):
        if self.running and self.call_count % 3 == 0:
            self.running_index = (self.running_index + 1) % 8

        elif self.jumping:
            if not self.falling:
                self.rect.bottom -= self.jump_speed

                if self.jump_speed >= self.gravity_up:
                    self.jump_speed -= self.gravity_up

                if self.rect.bottom < self.jump_limit:
                    self.jump_speed = 0

                    self.falling = True

            else:
                self.rect.bottom += self.jump_speed
                self.jump_speed += self.gravity_down

                if self.rect.bottom > GROUND_HEIGHT:
                    self.rect.bottom = GROUND_HEIGHT

                    self.jump_speed = 50

                    self.jumping_index = 0
                    self.running_index = 0

                    self.jumping = False
                    self.falling = False
                    self.running = True

            if self.call_count % 2 == 0 or self.call_count % 3 == 0:
                self.jumping_index = (self.jumping_index + 1) % 16

        elif self.idle and self.call_count % 3 == 0:
            self.idle_index = (self.idle_index + 1) % 10

        self.call_count = self.call_count + 1


class Score:
    def __init__(self):
        self.high_score_image, self.rect_high = load_image(
            "image/score/high_score.png", 35, 35
        )
        self.current_score_image, self.rect_current = load_image(
            "image/score/current_score.png", 35, 35
        )

        self.rect_high.topright = (SCREEN_WIDTH - 15, 20)
        self.rect_current.topright = (SCREEN_WIDTH - 15, 65)

        self.high_score = 0
        self.score = 0

        self.load()

        self.high_score_achieved = False

        self.call_count = 0

    def count(self):
        if self.call_count % 2 == 0:
            self.score += 1

            if self.high_score_achieved:
                self.high_score = self.score

            elif self.score > self.high_score:
                self.high_score = self.score
                self.high_score_achieved = True
                score_sound.play()

        self.call_count = self.call_count + 1

        if self.score % 500 >= 0 and self.score % 500 < 15 and self.score > 500:
            draw_text(
                "congratulation!",
                "font/northcliff_stencil.otf",
                70,
                (255, 0, 0),
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 5,
                "midtop",
            )
        # if Dino.check_coin_collision(Coin.get_coin(self)):
        # self.score += 50

    def draw(self):
        window.blit(self.high_score_image, self.rect_high)
        window.blit(self.current_score_image, self.rect_current)

        draw_text(
            str(self.high_score),
            "font/monofonto.ttf",
            28,
            (19, 130, 98),
            SCREEN_WIDTH - 60,
            20,
            "topright",
        )
        draw_text(
            str(self.score),
            "font/monofonto.ttf",
            28,
            (50, 130, 98),
            SCREEN_WIDTH - 60,
            65,
            "topright",
        )

    def load(self):
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except (IOError, ValueError):
            self.high_score = 0

    def save(self):
        if self.high_score_achieved:
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))


class GameOver:
    def __init__(self):
        self.replay_image, self.rect = load_image(
            "image/game_over/replay_0.png", 200, 60
        )

        self.rect.center = (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))

    def draw(self):
        draw_text(
            "GAME OVER",
            "font/northcliff_stencil.otf",
            80,
            (255, 0, 0),
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 3,
            "midtop",
        )
        window.blit(self.replay_image, self.rect)


def start_game():
    run = True
    play_again = False
    game_over = False

    game_speed = 15
    backgrounds = AllBackgrounds(game_speed)
    cactus = Cactus(game_speed)
    dino = Dino()
    score = Score()
    game_over_screen = GameOver()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if game_over:
                    if (
                        game_over_screen.rect.left < mx < game_over_screen.rect.right
                        and game_over_screen.rect.top
                        < my
                        < game_over_screen.rect.bottom
                    ):
                        play_again = True
                        run = False

        key = pygame.key.get_pressed()

        if key[K_SPACE] or key[K_UP]:
            if game_over:
                play_again = True
                run = False
            elif not dino.jumping:
                jump_sound.play()
                dino.jumping = True
                dino.running = False

                if dino.idle:
                    dino.idle = False

        backgrounds.draw()
        cactus.draw()
        dino.draw()
        score.draw()

        if game_over:
            game_over_screen.draw()

        else:
            if not dino.idle:
                score.count()

                backgrounds.update()
                cactus.update()

                if score.score % 120 == 0:
                    game_speed += 0.5
                    backgrounds.update_speed(game_speed)
                    cactus.update_speed(game_speed)
                    dino.jump_speed += 5

            dino.update()

            if dino.check_collision(cactus.get_cactus()):
                game_over = True
                game_over_screen.draw()
                game_over_sound.play()
                score.save()

        pygame.display.flip()

    return play_again


while PLAY_GAME:
    PLAY_GAME = start_game()
