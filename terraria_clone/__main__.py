import cocos
import pyglet

from terraria_clone.agents.ghost import Ghost


class GhostLand(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(GhostLand, self).__init__()
                
        background = cocos.sprite.Sprite ('assets/cyperpunk.png')
        self.add(background)
        background.position = 320, 240
        background.scale = 0.45

        self.agent = Ghost()
        self.agent.position = 320, 240
        self.add(self.agent)

    def on_mouse_motion(self, x, y, dx, dy):
        self.agent.move_to(x, y)

    def on_key_press (self, key, modifiers):
        if (key == pyglet.window.key.SPACE):
            self.agent.rotate()


cocos.director.director.init()
main_scene = cocos.scene.Scene(GhostLand())
cocos.director.director.run(main_scene)
