from module.protocol.network.message import Message


class ClientUIOpenedByObjectMessage(Message):
    def __init__(self):
        self.id = 2095
