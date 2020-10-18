import cocos

from terraria_clone.labels.hello_label import HelloLabel


class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):         
        super(HelloWorld, self).__init__(241, 247, 54, 255)
        
        label = HelloLabel()
        
        label.position = 320, 240

        self.add(label)

        ghost = cocos.sprite.Sprite('assets/ghost_idle_1.png')
        ghost.position = 470, 240
        ghost.scale = 0.5

        self.add(ghost, z=1)

        scale = cocos.actions.ScaleBy(3, duration=0.5)

        label.do(cocos.actions.Repeat(
            scale
            + cocos.actions.Reverse(scale)
        ))

        ghost.do(cocos.actions.Repeat(
            cocos.actions.Reverse(scale)
            + scale
            + (
                cocos.actions.RotateBy(45, 0.1)
                | cocos.actions.MoveBy((-200, 3), 0.1)
            )
            + cocos.actions.MoveBy((200, -3), .25)
        ))



cocos.director.director.init()
hello_layer = HelloWorld()
hello_layer.do(cocos.actions.Repeat(
    cocos.actions.RotateBy(360, duration=2.5)
))
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)
