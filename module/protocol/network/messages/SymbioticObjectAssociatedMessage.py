from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SymbioticObjectAssociatedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8203
        self.vars.append({"name": "hostUID", "type": "uint", "value": ""})
