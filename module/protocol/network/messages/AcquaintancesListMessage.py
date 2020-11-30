from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AcquaintancesListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1163
        self.acquaintanceList = {"type": "Vector.<AcquaintanceInformation>", "value": ""}
