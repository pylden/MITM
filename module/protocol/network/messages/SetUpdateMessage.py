from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SetUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1745
        self.vars.append({"name": "setId", "type": "uint", "value": ""})
        self.vars.append({"name": "setObjects", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "setEffects", "type": "Vector.<ObjectEffect>", "value": ""})
