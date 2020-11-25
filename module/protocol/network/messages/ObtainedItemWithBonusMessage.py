from module.protocol.network.message import Message


class ObtainedItemWithBonusMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2422
        self.bonusQuantity = {"type": "uint", "value": ""}
