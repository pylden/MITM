from module.protocol.network.message import Message


class ClientYouAreDrunkMessage(Message):
    def __init__(self):
        self.id = 1472
