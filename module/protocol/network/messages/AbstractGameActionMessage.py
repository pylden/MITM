from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AbstractGameActionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3972
        self.vars.append({"name": "actionId", "type": "uint", "value": ""})
        self.vars.append({"name": "sourceId", "type": "Number", "value": ""})
