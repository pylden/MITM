from module.protocol.network.message import Message


class ItemNoMoreAvailableMessage(Message):
    def __init__(self):
        self.id = 2884
