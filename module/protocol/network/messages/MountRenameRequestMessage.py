from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountRenameRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9887
        self.vars.append({"name": "name", "type": "String", "value": ""})
        self.vars.append({"name": "mountId", "type": "int", "value": ""})
