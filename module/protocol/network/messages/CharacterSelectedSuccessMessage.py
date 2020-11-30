from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterSelectedSuccessMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1931
        self.infos = {"type": "CharacterBaseInformations", "value": ""}
        self.isCollectingStats = {"type": "Boolean", "value": ""}
