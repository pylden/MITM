from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectUseInWorkshopMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2394
        self.objectUID = {"type": "uint", "value": ""}
        self.quantity = {"type": "int", "value": ""}
