from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StorageKamasUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4456
        self.vars.append({"name": "kamasTotal", "type": "Number", "value": ""})
