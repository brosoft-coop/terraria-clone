import cocos
import pyglet

from terraria_clone.levels.haunted_house import HauntedHouse

cocos.director.director.init()
cocos.director.director.show_FPS = True
main_scene = cocos.scene.Scene(HauntedHouse())
main_scene.scale = 4
cocos.director.director.run(main_scene)