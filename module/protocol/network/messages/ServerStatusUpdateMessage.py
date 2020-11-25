from module.protocol.network.message import Message


class ServerStatusUpdateMessage(Message):
    def __init__(self):
        self.id = 3937
