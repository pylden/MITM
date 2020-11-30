from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TitlesAndOrnamentsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7824
        self.titles = {"type": "Vector.<uint>", "value": ""}
        self.ornaments = {"type": "Vector.<uint>", "value": ""}
        self.activeTitle = {"type": "uint", "value": ""}
        self.activeOrnament = {"type": "uint", "value": ""}
