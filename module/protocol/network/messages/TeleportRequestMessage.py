from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TeleportRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1080
        self.vars.append({"name": "sourceType", "type": "uint", "value": ""})
        self.vars.append({"name": "destinationType", "type": "uint", "value": ""})
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
