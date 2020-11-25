from module.protocol.network.message import Message


class BasicWhoAmIRequestMessage(Message):
    def __init__(self):
        self.id = 5576
