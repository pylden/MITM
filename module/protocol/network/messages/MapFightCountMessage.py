from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapFightCountMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7990
        self.vars.append({"name": "fightCount", "type": "uint", "value": ""})
