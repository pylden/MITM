from module.protocol.network.message import Message


class FocusedExchangeReadyMessage(Message):
    def __init__(self):
        self.id = 9510
