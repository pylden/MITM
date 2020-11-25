from module.protocol.network.message import Message


class PlayerStatusUpdateRequestMessage(Message):
    def __init__(self):
        self.id = 6455
