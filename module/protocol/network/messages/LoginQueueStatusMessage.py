from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LoginQueueStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7010
        self.vars.append({"name": "position", "type": "uint", "value": ""})
        self.vars.append({"name": "total", "type": "uint", "value": ""})
