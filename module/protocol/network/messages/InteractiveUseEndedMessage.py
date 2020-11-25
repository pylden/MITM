from module.protocol.network.message import Message


class InteractiveUseEndedMessage(Message):
    def __init__(self):
        self.id = 785
