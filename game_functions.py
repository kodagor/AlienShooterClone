import sys
from time import sleep
import pygame
import os
# from random import randint
# from stars import Star
from alien import Alien
from bullet import Bullet


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """check for key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """check for button clicked and start game"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not stats.game_active:
            #hide pointer
            pygame.mouse.set_visible(False)

            # zero stats
            stats.reset_stats()
            stats.game_active = True

            # delete content of aliens and bullets lists
            aliens.empty()
            bullets.empty()

            # create new fleet and center the ship
            create_fleet(ai_settings, screen, ship, aliens)
            ship.center_ship()


def check_keydown_events(event, ai_settings, stats, screen, ship, bullets):
    """reaction to kye press"""
    if event.key == pygame.K_ESCAPE:
        # quit game
        sys.exit()
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        # move ship on right
        ship.moving_right = True
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        # move left
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        # shoot
        fire_bullets(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_p:
        if stats.game_active:
            stats.game_active = False
        else:
            stats.game_active = True


def check_keyup_events(event, ship):
    """reaction to ket release"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        # move ship on right
        ship.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        # move left
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """update pictures on the screen and moving to new screen"""
    # refreshing screen during each loop iteration
    screen.fill(ai_settings.bg_color)

    # stars before (under) everything
    # stars.draw(screen)

    # showing again bullets under ship and aliens layers
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    # displaying last modified screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """update bullets pos and removing these outside the screen"""

    # update bullet pos
    bullets.update()

    # remove bullets outside the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))   # check in console if bullets are disappear correctly
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """reaction to collision between alien and bullet"""
    # removing aliens and bullets if collision was happen
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # remove remaining bullets and create new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullets(ai_settings, screen, ship, bullets):
    """shoot a bullet, if you can"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """number of aliens in row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """creating full alien fleet"""
    # create an alien and aliens in one row
    # dist between aliens is equal alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """creating full alien fleet"""
    # create an alien and aliens in one row
    # dist between aliens is equal alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create first aliens row
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_rows(ai_settings, ship_height, alien_height):
    """how rows on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    """reaction after reaching screen edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_directions(ai_settings, aliens)
            break


def change_fleet_directions(ai_settings, aliens):
    """move fleet down and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """check if fleet is near edges an update alien fleet pos"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # check collision between aliens and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # looking for aliens going to thoe bottom edge
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Reaction after hitting ship"""
    # reduce ships_left
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # delete content of lists aliens and bullets
        aliens.empty()
        bullets.empty()

        # create new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
        print(stats.ships_left)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check, if whichever alien has hit the bottom edge"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # the same as collide with ship
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


# def get_number_stars_x(ai_settings, star_width):
#     """number of stars in one row"""
#     available_space_x = ai_settings.screen_width - star_width
#     number_stars_x = int(available_space_x / star_width)
#     return number_stars_x
#
#
# def create_star(ai_settings, screen, stars, star_number, row_number):
#     """creating a star and put in the row"""
#     random_num = randint(-20, 100)
#     star = Star(ai_settings, screen)
#     star_width = star.rect.width
#     star.x = star_width + random_num * star_width * star_number
#     star.rect.x = star.x
#     star.rect.y = star.rect.height + random_num * star.rect.height * row_number
#     stars.add(star)
#
#
# def create_stars(ai_settings, screen, stars):
#     """creating many stars"""
#     # creating a star like the alien
#     star = Star(ai_settings, screen)
#     number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
#     number_rows = get_number_rows_stars(ai_settings, star.rect.height)
#
#     # stars rows
#     for row_number in range(number_rows):
#         for star_number in range(number_stars_x):
#             # create a star and put in the row
#             create_star(ai_settings, screen, stars, star_number, row_number)
#
#
# def get_number_rows_stars(ai_settings, star_height):
#     """creating rows that fill entire screen"""
#     available_space_y = ai_settings.screen_height
#     number_rows = int(available_space_y / (2 * star_height))
#     return number_rows


# def stars_down(ai_settings, stars):
#     """move down the stars"""
#     for star in stars.sprites():
#         star.rect.y += ai_settings.star_speed_factor


# def check_star_edge(ai_settings, screen, stars, row_number):
#     """reaction after reaching screen edge"""
#     star = Star(ai_settings, screen)
#     number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
#
#     for star in stars.sprites():
#         if star.check_edge():
#             for star_number in range(number_stars_x):
#                 # create a star and put in the row
#                 create_star(ai_settings, screen, stars, star_number, row_number)


# def update_stars(stars):
#     """update stars pos"""
#     # stars_down(ai_settings, stars)
#     # check_star_edge(ai_settings, screen, stars, row_number=1)
#     stars.update()

