from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AbstractPartyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 555
        self.partyId = {"type": "uint", "value": ""}
