from module.protocol.network.messages.EmotePlayAbstractMessage import EmotePlayAbstractMessage


class EmotePlayMessage(EmotePlayAbstractMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        EmotePlayAbstractMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8116
        self.actorId = {"type": "Number", "value": ""}
        self.accountId = {"type": "uint", "value": ""}
