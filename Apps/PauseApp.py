import pygame
from App import App
from Designs.PauseDesign import PauseDesign
from EventHandler import EventHandler
from Screen import Screen

class PauseApp(App, PauseDesign):
    @classmethod
    def back_button(cls):
        """Выход из паузы"""
        cls.end()

    @classmethod
    def exit_button(cls):
        """Выход из игры"""
        cls.redirect("MainMenuApp", use_deque=False)

    @classmethod
    def settings_button(cls):
        """Выход из паузы"""
        pass



    @classmethod
    def render(cls):
        """Отрисовка экрана"""
        Screen.display.blit(cls.gameFrame, (0, 0))
        cls.allSprites.update()
        cls.allSprites.draw(Screen.display)
        Screen.update_display()


    @classmethod
    def loop(cls, *args, **kwargs):
        cls.gameFrame = kwargs["penis"]

        cls.init_textures()

        cls.link_function_to_button("backButton", cls.back_button)
        cls.link_function_to_button("exitButton", cls.exit_button)
        cls.link_function_to_button("settingsButton", cls.settings_button)

        cls.init_sprites_and_groups()

        while cls.running:
            """main loop of app"""

            EventHandler.tick()  # clock update

            EventHandler.update(cls)  # events and groups update

            cls.render()  # app update

            cls.check_events()  # local events check

    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cls.end()
                elif event.key == pygame.K_RETURN:
                    cls.enter_button()

