from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MigratedServerListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5457
        self.vars.append({"name": "migratedServerIds", "type": "Vector.<uint>", "value": ""})
