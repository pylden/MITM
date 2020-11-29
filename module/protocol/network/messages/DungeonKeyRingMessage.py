from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonKeyRingMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6151
        self.vars.append({"name": "availables", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "unavailables", "type": "Vector.<uint>", "value": ""})
