import pygame
from App import App
from Screen import Screen
from EventHandler import EventHandler
from Designs.EndDesign import EndDesign


class EndApp(App, EndDesign):
    """Экран окончания игры"""

    image: pygame.surface
    score: int

    @classmethod
    def exit_button(cls):
        """Выход из экрана"""
        cls.redirect("MainMenuApp")
        cls.end()

    @classmethod
    def loop(cls, *args, **kwargs):

        cls.image = kwargs["image"]
        cls.score = kwargs["score"]

        cls.init_textures()

        cls.link_function_to_button("exitButton", cls.exit_button)

        cls.init_sprites_and_groups()

        cls.get_element("textLabel3").write(cls.score)

        cls.render()

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
                    cls.exit_button()

    @classmethod
    def render(cls):
        """Отрисовка экрана"""
        cls.allSprites.update()
        Screen.display.blit(cls.image, (0, 0))
        cls.allSprites.draw(Screen.display)
        Screen.update_display()
