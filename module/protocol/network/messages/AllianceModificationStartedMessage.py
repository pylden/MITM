from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceModificationStartedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2652
        self.vars.append({"name": "canChangeName", "type": "Boolean", "value": ""})
        self.vars.append({"name": "canChangeTag", "type": "Boolean", "value": ""})
        self.vars.append({"name": "canChangeEmblem", "type": "Boolean", "value": ""})
