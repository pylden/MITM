from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildPaddockBoughtMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9535
        self.vars.append({"name": "paddockInfo", "type": "PaddockContentInformations", "value": ""})
