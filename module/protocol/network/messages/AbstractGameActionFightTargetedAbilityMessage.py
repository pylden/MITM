from module.protocol.network.message import Message


class AbstractGameActionFightTargetedAbilityMessage(Message):
    def __init__(self):
        self.id = 4295
