from module.protocol.network.messages.ObjectUseMessage import ObjectUseMessage


class ObjectUseOnCharacterMessage(ObjectUseMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ObjectUseMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1575
        self.characterId = {"type": "Number", "value": ""}
