from module.protocol.network.message import Message


class ObjectDropMessage(Message):
    def __init__(self):
        self.id = 5169
