from module.protocol.network.message import Message


class InventoryWeightMessage(Message):
    def __init__(self):
        self.id = 1306