from module.protocol.network.message import Message


class SetCharacterRestrictionsMessage(Message):
    def __init__(self):
        self.id = 5009
