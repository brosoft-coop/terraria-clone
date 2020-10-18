import cocos

from terraria_clone.agents.ghost import Ghost


cocos.director.director.init()
main_scene = cocos.scene.Scene(Ghost())
cocos.director.director.run(main_scene)
