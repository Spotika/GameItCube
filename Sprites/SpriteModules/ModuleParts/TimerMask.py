from Sprites.SpriteModules.SpriteModule import SpriteModule
from Sprites.ImageLabel import ImageLabel
from Colors import Colors
from Sprites.TextLabel import TextLabel


class TimerMask(SpriteModule):
    timer = None

    def __init__(self, position, dims, opacity=100):
        super().__init__(position, dims, layer=300)

        self.set_design({
            "mask": ImageLabel((0, 0), dims, color=Colors.BLACK, layer=0),
            "timer": TextLabel((dims[0] // 4, dims[0] // 4), (dims[0] // 2, dims[1] // 2), layer=100)
        })
        self.get_image().set_alpha(opacity)
        self.init_design()

    def link_timer(self, timer) -> None:
        self.timer = timer

    def update(self):
        if self.timer is not None:
            delay = self.timer()
            if delay == 0:
                self.hide()
            else:
                self.show()
                self.get_design("timer").write(delay)
        else:
            self.hide()
        self.update_image_by_design()
        self.update_design()
