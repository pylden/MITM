from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TitlesAndOrnamentsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7824
        self.vars.append({"name": "titles", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "ornaments", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "activeTitle", "type": "uint", "value": ""})
        self.vars.append({"name": "activeOrnament", "type": "uint", "value": ""})
