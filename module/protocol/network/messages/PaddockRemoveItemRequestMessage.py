from module.protocol.network.message import Message


class PaddockRemoveItemRequestMessage(Message):
    def __init__(self):
        self.id = 6943
