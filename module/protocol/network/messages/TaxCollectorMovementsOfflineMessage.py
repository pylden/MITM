from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorMovementsOfflineMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2499
        self.movements = {"type": "Vector.<TaxCollectorMovement>", "value": ""}
