from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntFinishedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4291
        self.vars.append({"name": "questType", "type": "uint", "value": ""})
