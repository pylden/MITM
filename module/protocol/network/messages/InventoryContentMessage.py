from module.protocol.network.message import Message


class InventoryContentMessage(Message):
    def __init__(self):
        self.id = 4140
