from module.protocol.network.messages.EmotePlayAbstractMessage import EmotePlayAbstractMessage


class EmotePlayMessage(EmotePlayAbstractMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        EmotePlayAbstractMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8116
        self.vars.append({"name": "actorId", "type": "Number", "value": ""})
        self.vars.append({"name": "accountId", "type": "uint", "value": ""})
