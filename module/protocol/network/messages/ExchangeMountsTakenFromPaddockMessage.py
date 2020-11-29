from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountsTakenFromPaddockMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8081
        self.vars.append({"name": "name", "type": "String", "value": ""})
        self.vars.append({"name": "worldX", "type": "int", "value": ""})
        self.vars.append({"name": "worldY", "type": "int", "value": ""})
        self.vars.append({"name": "ownername", "type": "String", "value": ""})
