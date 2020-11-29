from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StartupActionFinishedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3256
        self.vars.append({"name": "success", "type": "Boolean", "value": ""})
        self.vars.append({"name": "actionId", "type": "uint", "value": ""})
        self.vars.append({"name": "automaticAction", "type": "Boolean", "value": ""})
