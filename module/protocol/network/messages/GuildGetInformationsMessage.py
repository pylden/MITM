from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildGetInformationsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3578
        self.infoType = {"type": "uint", "value": ""}
