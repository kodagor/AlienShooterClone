import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
import game_functions as gf


def run_game():
    # pre_init mixer to avoid music and sounds delay
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load('music/p_music1.mp3')

    # game init and creating an object for the screen
    pygame.init()

    pygame.mixer.music.play(-1)
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN, 32)
    pygame.display.set_caption("Hardcore Galactic Shooter")

    # create button "Play"
    play_button = Button(ai_settings, screen, "Play")

    # game stats
    stats = GameStats(ai_settings)
    # scoreboard
    sb = Scoreboard(ai_settings, screen, stats)

    # create a star
    # star = Star(ai_settings, screen)
    # now the stars
    # stars = Group()

    # here is method creating the stars
    # gf.create_stars(ai_settings, screen, stars)

    # creating the ship
    ship = Ship(ai_settings, screen)

    # creating group for holding bullets
    bullets = Group()

    #  and group fo alien fleet
    aliens = Group()
    # create fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # main loop for game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        # gf.update_stars(stars)
        if stats.game_active:
            # need to update ship position according to his movement
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

