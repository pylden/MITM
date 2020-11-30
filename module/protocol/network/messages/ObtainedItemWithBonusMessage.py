from module.protocol.network.messages.ObtainedItemMessage import ObtainedItemMessage


class ObtainedItemWithBonusMessage(ObtainedItemMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ObtainedItemMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2422
        self.bonusQuantity = {"type": "uint", "value": ""}
