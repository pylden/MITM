from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntDigRequestAnswerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7127
        self.vars.append({"name": "questType", "type": "uint", "value": ""})
        self.vars.append({"name": "result", "type": "uint", "value": ""})
