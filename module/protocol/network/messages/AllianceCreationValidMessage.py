from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceCreationValidMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8739
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
        self.allianceEmblem = {"type": "GuildEmblem", "value": ""}
