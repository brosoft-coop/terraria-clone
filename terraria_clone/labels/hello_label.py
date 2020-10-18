import cocos

class HelloLabel(cocos.text.Label):
    def __init__(self):
        super(HelloLabel, self).__init__(
            'Hello dude',
            font_name="Arial",
            font_size=30,
            anchor_x='center', 
            anchor_y='center',
            color=(230, 20, 20, 255)
        )