from module.protocol.network.message import Message


class InventoryWeightMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1306
        self.inventoryWeight = {"type": "uint", "value": ""}
        self.shopWeight = {"type": "uint", "value": ""}
        self.weightMax = {"type": "uint", "value": ""}
