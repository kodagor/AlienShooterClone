import pygame.sysfont


class Button:

    def __init__(self, ai_setting, screen, msg):
        """init button box attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # define dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 200)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # create rect fo button and centered it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # message on button
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """generate txt image"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """display empty button and then message on it"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

