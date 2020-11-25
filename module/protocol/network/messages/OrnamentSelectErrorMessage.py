from module.protocol.network.message import Message


class OrnamentSelectErrorMessage(Message):
    def __init__(self):
        self.id = 9564
