import cocos


class Ghost(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(Ghost, self).__init__()
        self.sprite = cocos.sprite.Sprite('assets/ghost_idle_1.png')
        self.sprite.scale = 0.1
        self.add(self.sprite)
        self.position = 320, 240

    def on_mouse_motion(self, x, y, dx, dy):
        self.position = x, y