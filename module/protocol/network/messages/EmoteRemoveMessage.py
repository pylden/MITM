from module.protocol.network.message import Message


class EmoteRemoveMessage(Message):
    def __init__(self):
        self.id = 2580