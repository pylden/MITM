from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceJoinedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6500
        self.allianceInfo = {"type": "AllianceInformations", "value": ""}
        self.enabled = {"type": "Boolean", "value": ""}
        self.leadingGuildId = {"type": "uint", "value": ""}
