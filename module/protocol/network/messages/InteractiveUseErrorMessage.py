from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InteractiveUseErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9202
        self.vars.append({"name": "elemId", "type": "uint", "value": ""})
        self.vars.append({"name": "skillInstanceUid", "type": "uint", "value": ""})
