from module.protocol.network.message import Message


class GameActionFightTriggerEffectMessage(Message):
    def __init__(self):
        self.id = 2730
