from module.protocol.network.messages.NetworkMessage import NetworkMessage


class KnownZaapListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9552
        self.vars.append({"name": "destinations", "type": "Vector.<Number>", "value": ""})
