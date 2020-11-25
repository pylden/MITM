from module.protocol.network.message import Message


class StatedElementUpdatedMessage(Message):
    def __init__(self):
        self.id = 4169
