from module.protocol.network.message import Message


class InteractiveUseWithParamRequestMessage(Message):
    def __init__(self):
        self.id = 4240
