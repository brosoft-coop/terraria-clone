import cocos


class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):         
        super(HelloWorld, self).__init__(241, 247, 54, 255)
        
        label = cocos.text.Label(
            'Hello dude',
            font_name="Arial",
            font_size=30,
            anchor_x='center', 
            anchor_y='center',
            color=(255, 0, 255, 255)
        )
        
        label.position = 320, 240

        self.add(label)



cocos.director.director.init()
hello_layer = HelloWorld()
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)
