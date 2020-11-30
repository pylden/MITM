from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildCharacsUpgradeRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6519
        self.charaTypeTarget = {"type": "uint", "value": ""}
