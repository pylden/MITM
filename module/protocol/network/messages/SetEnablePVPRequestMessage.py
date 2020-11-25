from module.protocol.network.message import Message


class SetEnablePVPRequestMessage(Message):
    def __init__(self):
        self.id = 4606
