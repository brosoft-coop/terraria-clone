import cocos
import pyglet

class HauntedHouse(cocos.layer.ScrollingManager):
    is_event_handler = True

    def __init__(self):
        super(HauntedHouse, self).__init__()
        resouce = cocos.tiles.load('assets/hounted-house-scene.tmx')
        self.add(resouce['brick'])
        self.add(resouce['breackness'])
        self.add(resouce['dirt'])
        self.add(resouce['dirt-2'])
        self.add(resouce['ground-tiles'])
        self.add(resouce['ground-dirt'])
        self.add(resouce['tiles'])
        self.position = 0, 0
        self.set_focus(*self.position)

    def on_draw(self):
        pyglet.gl.glTexParameteri(
            pyglet.gl.GL_TEXTURE_2D,
            pyglet.gl.GL_TEXTURE_MAG_FILTER,
            pyglet.gl.GL_NEAREST
        ) 
        pyglet.gl.glTexParameteri(
            pyglet.gl.GL_TEXTURE_2D,
            pyglet.gl.GL_TEXTURE_MIN_FILTER,
            pyglet.gl.GL_NEAREST
        ) 

    
    def on_key_press (self, key, modifiers):
        x, y = self.position;

        if (key == pyglet.window.key.W):
            y += 8

        if (key == pyglet.window.key.S):
            y -= 8 

        if (key == pyglet.window.key.A):
            x -= 8

        if (key == pyglet.window.key.D):
            x += 8 

        self.position = x, y
        print(self.position)
        self.set_focus(*self.position)
        

