import cocos


class Ghost(cocos.sprite.Sprite):
    def __init__(self):
        super(Ghost, self).__init__('assets/ghost_idle_1.png')
        self.scale = 0.5