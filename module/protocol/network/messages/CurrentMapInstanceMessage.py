from module.protocol.network.message import Message


class CurrentMapInstanceMessage(Message):
    def __init__(self):
        self.id = 4034
