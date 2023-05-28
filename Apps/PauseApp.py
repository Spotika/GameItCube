import pygame
from App import App
from EventHandler import EventHandler
from Designs.PauseDesign import PauseDesign
from Screen import Screen


class PauseApp(App, PauseDesign):
    """Пауза"""

    image: pygame.surface

    @classmethod
    def exit_button(cls):
        """Выход из игры"""
        EventHandler.push_to_stream("PauseApp", "exit")
        cls.end()

    @classmethod
    def enter_button(cls):
        """Возврат в игру"""
        cls.end()

    @classmethod
    def loop(cls, *args, **kwargs):

        cls.image = kwargs["image"]

        cls.init_textures()

        cls.link_function_to_button("exitButton", cls.exit_button)
        cls.link_function_to_button("enterButton", cls.enter_button)

        cls.init_sprites_and_groups()

        cls.render()  # вызывается единожды тк картинка паузы статична

        while cls.running:
            """main loop of app"""

            EventHandler.tick()  # clock update

            EventHandler.update(cls)  # events and groups update

            cls.check_events()  # local events check

    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cls.exit_button()  # Выйти из игры
                elif event.key == pygame.K_RETURN:
                    cls.enter_button()  # Вернуться в игру

    @classmethod
    def render(cls):
        """Отрисовка экрана"""
        cls.allSprites.update()
        Screen.display.blit(cls.image, (0, 0))
        cls.allSprites.draw(Screen.display)
        Screen.update_display()
