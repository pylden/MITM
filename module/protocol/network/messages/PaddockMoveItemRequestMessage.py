from module.protocol.network.message import Message


class PaddockMoveItemRequestMessage(Message):
    def __init__(self):
        self.id = 815
