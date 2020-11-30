from module.protocol.network.messages.ObjectUseMessage import ObjectUseMessage


class ObjectUseMultipleMessage(ObjectUseMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ObjectUseMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3678
        self.quantity = {"type": "uint", "value": ""}
