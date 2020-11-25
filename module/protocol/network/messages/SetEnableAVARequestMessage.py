from module.protocol.network.message import Message


class SetEnableAVARequestMessage(Message):
    def __init__(self):
        self.id = 4687
