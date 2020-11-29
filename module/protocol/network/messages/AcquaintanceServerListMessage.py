from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AcquaintanceServerListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 137
        self.vars.append({"name": "servers", "type": "Vector.<uint>", "value": ""})
