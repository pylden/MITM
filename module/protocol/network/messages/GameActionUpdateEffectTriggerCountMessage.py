from module.protocol.network.message import Message


class GameActionUpdateEffectTriggerCountMessage(Message):
    def __init__(self):
        self.id = 4310
