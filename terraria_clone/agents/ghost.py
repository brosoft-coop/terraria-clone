import cocos


class Ghost(cocos.sprite.Sprite):
    def __init__(self):
        super(Ghost, self).__init__('assets/ghost_idle_1.png')
        self.scale = 3

    def move_to(self, x, y):
        self.position = x, y

    def rotate(self):
        self.do(cocos.actions.RotateBy(90, 0.2))
