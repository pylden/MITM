from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MimicryObjectEraseRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1801
        self.vars.append({"name": "hostUID", "type": "uint", "value": ""})
        self.vars.append({"name": "hostPos", "type": "uint", "value": ""})
