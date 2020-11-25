from module.protocol.network.message import Message


class ShowCellRequestMessage(Message):
    def __init__(self):
        self.id = 7647
