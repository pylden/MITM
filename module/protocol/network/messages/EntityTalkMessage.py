from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EntityTalkMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5442
        self.vars.append({"name": "entityId", "type": "Number", "value": ""})
        self.vars.append({"name": "textId", "type": "uint", "value": ""})
        self.vars.append({"name": "parameters", "type": "Vector.<String>", "value": ""})
