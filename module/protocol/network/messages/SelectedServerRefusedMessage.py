from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SelectedServerRefusedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6211
        self.vars.append({"name": "serverId", "type": "uint", "value": ""})
        self.vars.append({"name": "error", "type": "uint", "value": ""})
        self.vars.append({"name": "serverStatus", "type": "uint", "value": ""})
