from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChatSmileyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2519
        self.vars.append({"name": "entityId", "type": "Number", "value": ""})
        self.vars.append({"name": "smileyId", "type": "uint", "value": ""})
        self.vars.append({"name": "accountId", "type": "uint", "value": ""})
