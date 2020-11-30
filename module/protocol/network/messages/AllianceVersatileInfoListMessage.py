from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceVersatileInfoListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2433
        self.alliances = {"type": "Vector.<AllianceVersatileInformations>", "value": ""}
