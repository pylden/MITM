from module.protocol.network.message import Message


class ServerOptionalFeaturesMessage(Message):
    def __init__(self):
        self.id = 2305
