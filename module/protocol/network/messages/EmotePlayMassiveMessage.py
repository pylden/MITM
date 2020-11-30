from module.protocol.network.messages.EmotePlayAbstractMessage import EmotePlayAbstractMessage


class EmotePlayMassiveMessage(EmotePlayAbstractMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        EmotePlayAbstractMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9926
        self.actorIds = {"type": "Vector.<Number>", "value": ""}
