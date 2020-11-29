from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountEmoteIconUsedOkMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4039
        self.vars.append({"name": "mountId", "type": "int", "value": ""})
        self.vars.append({"name": "reactionType", "type": "uint", "value": ""})
