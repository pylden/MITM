from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightStartMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9280
        self.vars.append({"name": "idols", "type": "Vector.<Idol>", "value": ""})
